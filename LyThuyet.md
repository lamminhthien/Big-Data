1. Nêu các đặc trưng cơ bản của dữ liệu lớn. Với mỗi đặc trưng hãy nêu ví dụ thực tế để
minh họa:
2. Nêu các lợi ích của xử lý dữ liệu lớn. Nêu ví dụ thực tế minh họa.
3. Nêu các thách thức khi xử lý dữ liệu lớn.
4. Trình bày các cách tiếp cận chính hiện nay để xử lý dữ liệu lớn.
5. Trình bày vắn tắt các đặc điểm chính của Hadoop. Nêu các ưu điểm, nhược điểm chính
của Hadoop.
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
