1. Nêu các đặc trưng cơ bản của dữ liệu lớn. Với mỗi đặc trưng hãy nêu ví dụ thực tế để
minh họa:
![image](https://user-images.githubusercontent.com/99172799/168302966-d7902d2a-9d2d-48ae-a182-9323af3f84b3.png)
![image](https://user-images.githubusercontent.com/99172799/168303032-7514980b-8ea0-4cdb-b7fb-ad37f4099142.png)
![image](https://user-images.githubusercontent.com/99172799/168303164-1d2b212f-8aba-4b1a-9e12-e4778a4cdb50.png)
![image](https://user-images.githubusercontent.com/99172799/168303245-19a54844-ccc7-4243-81ea-14ea9a2ba7dc.png)
2. Nêu các lợi ích của xử lý dữ liệu lớn. Nêu ví dụ thực tế minh họa.
![image](https://user-images.githubusercontent.com/99172799/168303299-850753ce-1246-4cd7-92fa-c827bee5ac3e.png)
![image](https://user-images.githubusercontent.com/99172799/168303343-e8041a67-561f-4e22-9160-b5e1b24b270a.png)
4. Nêu các thách thức khi xử lý dữ liệu lớn.
![image](https://user-images.githubusercontent.com/99172799/168303403-6537ba88-5d59-444e-9f36-8d32a0eda8cd.png)
6. Trình bày các cách tiếp cận chính hiện nay để xử lý dữ liệu lớn.
7. Trình bày vắn tắt các đặc điểm chính của Hadoop. Nêu các ưu điểm, nhược điểm chính
của Hadoop.
![image](https://user-images.githubusercontent.com/99172799/168300427-bc56d61c-bc71-4ccf-8637-7e234cc1b16a.png
![image](https://user-images.githubusercontent.com/99172799/168300606-235e43e7-0a23-44ef-9014-acb14687b966.png)
https://data-flair.training/blogs/13-limitations-of-hadoop/
**Nhược điểm**
![image](https://user-images.githubusercontent.com/99172799/168300922-7649c13d-747a-47a7-bf2e-25822941190e.png)
![image](https://user-images.githubusercontent.com/99172799/168301152-91cc6db1-301a-499e-bb94-93abfc63d2e2.png)
![image](https://user-images.githubusercontent.com/99172799/168301211-300c443f-e849-4507-aaba-c9e5c7caddb7.png)
![image](https://user-images.githubusercontent.com/99172799/168301393-4be1028b-5cab-4e04-856d-f0defb1054d7.png)
![image](https://user-images.githubusercontent.com/99172799/168301505-2e21a70d-bdd5-454f-b678-83bb16367c8b.png)

6. Trình bày vắn tắt các thành phần chính của Hadoop.
![image](https://user-images.githubusercontent.com/99172799/168297826-60bc381a-1475-4ab6-8d14-e7f7f1e3e5f1.png)
![image](https://user-images.githubusercontent.com/99172799/168297869-ace6d226-8d23-4327-b722-30650e8f5907.png)
![image](https://user-images.githubusercontent.com/99172799/168298044-9e3abcea-832a-4f10-9693-8ca40daa71e5.png)
7. Mô tả mô hình lập trình MapReduce. Trình bày vắn tắt luồng xử lý dữ liệu trong
MapReduce.
## Giải pháp Big Data: Hadoop <a name="bigdata_approach"/>

Nền tảng Hadoop cho phép triển khai các ứng dụng xử lý dữ liệu lớn (hàng TB) song song trên các cụm (cluster) lên đến hàng ngàn máy tính với độ tin cậy và khả năng chịu lỗi cao.
### Luồng xử lý của Hadoop MapReduce
Mô hình MapReduce chia tác vụ xử lý thành 2 pha: map và reduce. Với mỗi pha xử lý cần có 1 chương trình tương ứng: mapper và reducer. Cần phải lập trình mapper và reducer để xử lý theo yêu cầu bài toán.
#### Map
Khi bắt đầu xử lý, dữ liệu vào sẽ được chia nhỏ thành nhiều phần, mỗi phần được gửi đến một máy trạm riêng biệt. Mỗi máy trạm thực thi chương trình mapper trên phần dữ liệu nhận được.
Chương trình mapper đọc dữ liệu vào và chuyển thành các cặp <key, value>.
Giá trị của <key, value> do người lập trình xác định tùy theo yêu cầu bài toán. 
Ví dụ, với bài toán đếm từ, cặp <key, value> là <word, count>. Với mỗi từ đọc được, chương trình mapper xuất ra cặp giá trị <word, 1>. Các cặp <word, 1> sẽ được gộp và nhóm lại, những cặp <word, 1> giống nhau sẽ được nhóm lại và gửi đến một máy trạm riêng lẻ để xử lý ở pha reduce.
<br>
#### Reduce
Chương trình reducer xử lý các cặp <key, value> và rút gọn chúng theo cách mong muốn. 
Ví dụ, để đếm số lần xuất hiện của mỗi từ, chương trình reducer sẽ cộng giá trị của tất cả các cặp <word, 1> trùng nhau.

| <img src="figs/MapReduce.png" width="70%"/> | 
|:--:| 
| Minh họa giải quyết bài toán đếm từ với mô hình MapReduce. *Image source: https://bit.ly/3gfU6te* |
![image](https://user-images.githubusercontent.com/99172799/168297743-89c52639-ffc2-4f62-98f8-fc5407b13cfb.png)
8. Trình bày các đặc điểm chính của nền tảng Apache Spark.
![image](https://user-images.githubusercontent.com/99172799/168297573-8ccf974a-f9e5-494a-a511-d9af59b48577.png)
![image](https://user-images.githubusercontent.com/99172799/168297601-222904f1-73df-4922-8d08-c6a125d4772e.png)
9. Trình bày các điểm khác biệt chính trong mô hình xử lý của Spark so với MapReduce.
![image](https://user-images.githubusercontent.com/99172799/168297133-14c41c7f-bbe1-4c8e-b9ae-6bf714ab831c.png)
![image](https://user-images.githubusercontent.com/99172799/168297180-7da81eee-9798-42e4-9761-ee552c5af619.png)
![image](https://user-images.githubusercontent.com/99172799/168297214-4f68f23d-87ed-4480-8da4-f6db7d7444f4.png)
10. Trình bày các thành phần chính của nền tảng Apache Spark.
    - Apache Spark Core
        - Là hệ thống cốt lõi thực thi tổng quát, **làm cơ sở xây dựng các chức năng khác**.
        - Cung cấp tính năng tính toán trong bộ nhớ (In-Memory computing) và tham chiếu dữ liệu trên bộ nhớ ngoài.
    - Spark SQL
        - Là thành phần được xây dựng trên nền Spark Core, cung cấp tính năng trừu tượng hóa dữ liệu (data abstraction) gọi là SchemaRDD, cho phép xử lý dữ liệu có cấu trúc và bán cấu trúc.
    - Spark Streaming
        - Spark Streaming khai thác tính năng lập lịch nhanh của Spark Core để thực hiện các tác vụ xử lý luồng (streaming). Dữ liệu được chia thành các gói nhỏ và thực hiên chuyển đổi RDD trên chúng.
        - MLlib (Machine Learning Library)
        - Là nền tảng học máy phân tán trên Spark.
    - GraphX
        - Là nền tảng xử lý đồ thị phân tán (distributed graph-processing) trên Spark.
