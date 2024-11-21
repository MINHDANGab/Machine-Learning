import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F 
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        #convolution layer
        self.conv1 = nn.Conv2d(in_channels=1,out_channels=6,kernel_size=5,stride=1,padding=0)
        self.conv2 = nn.Conv2d(in_channels=6,out_channels=16,kernel_size = 5,stride=1, padding=0)
        #pooling layer
        self.pool = nn.MaxPool2d(kernel_size=2,stride = 2)
        #fully connected layer
        self.fc1 = nn.Linear(in_features=16*4*4,out_features=120)
        self.fc2 = nn.Linear(in_features=120,out_features=84)
        self.fc3 = nn.Linear(in_features=84,out_features=10)
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16*4*4)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
#normalize data    
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean=(0.5,),std=(0.5,))])
# chuyen thanh tensor va normalize voi mean = 0,5 std = 0,5


dataset = torchvision.datasets.MNIST(root = './data',train = True, download= True, transform = transform)
#tai dataset MNIST sau do nornamlize

trainloader = torch.utils.data.DataLoader(dataset,batch_size=64, shuffle = True)
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)
  

# Tạo đối tượng CNN
model = CNN()

# Định nghĩa hàm mất mát và bộ tối ưu
costly = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Huấn luyện mô hình
for epoch in range(10):  # Số epoch bạn muốn chạy
    
    for i, data in enumerate(trainloader, 0): # i la index cua mini-batch
        inputs, labels = data # data la 1 tuple(input_tensor[64,1,28,28],label_tensor[64,1,1,1])

        # Khởi tạo gradient về 0
        optimizer.zero_grad()

       
        #tinh toand dau ra cua mo hinh
        outputs = model(inputs) 
        #input la tensor co kich thuoc [64,1,28,28]
        #output la 1 tensor co kich thuoc [64,10,1,1]
        
        ## Tính toán hàm mất mát
        loss = costly(outputs, labels)
        
        # Tính toán gradient
        loss.backward()
        
        ## Cập nhật trọng số dựa trên gradient đã tính
        optimizer.step()

    print(f"Ket thuc epoch thu {epoch+1}")

print('Đã hoàn thành huấn luyện')

# Đánh giá mô hình trên tập test
'''correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = model(images)
        max_value, predicted = torch.max(outputs.data, 1) #torch.max(outputs.data,1) = (max_value, index_of_max_value)
        total += labels.size(0)#dem so labels
        correct += (predicted == labels).sum().item()#dem so predict dung

print(f'Accuracy của mạng trên tập test: {100 * correct / total:.2f}%')'''
#torch.save(model.state_dict(), 'cnn_model_weights.pt')  # Lưu chỉ trọng số vào file cnn_model_weights.pt
torch.save(model, 'cnn_model.pt')  # Lưu toàn bộ mô hình vào file cnn_model.pt




