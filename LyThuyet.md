1. Nêu các đặc trưng cơ bản của dữ liệu lớn. Với mỗi đặc trưng hãy nêu ví dụ thực tế để
minh họa:
2. Nêu các lợi ích của xử lý dữ liệu lớn. Nêu ví dụ thực tế minh họa.
3. Nêu các thách thức khi xử lý dữ liệu lớn.
4. Trình bày các cách tiếp cận chính hiện nay để xử lý dữ liệu lớn.
5. Trình bày vắn tắt các đặc điểm chính của Hadoop. Nêu các ưu điểm, nhược điểm chính
của Hadoop.
6. Trình bày vắn tắt các thành phần chính của Hadoop.
7. Mô tả mô hình lập trình MapReduce. Trình bày vắn tắt luồng xử lý dữ liệu trong
MapReduce.
8. Trình bày các đặc điểm chính của nền tảng Apache Spark.
9. Trình bày các điểm khác biệt chính trong mô hình xử lý của Spark so với MapReduce.
![image](https://user-images.githubusercontent.com/99172799/168297133-14c41c7f-bbe1-4c8e-b9ae-6bf714ab831c.png)
![image](https://user-images.githubusercontent.com/99172799/168297180-7da81eee-9798-42e4-9761-ee552c5af619.png)
![image](https://user-images.githubusercontent.com/99172799/168297214-4f68f23d-87ed-4480-8da4-f6db7d7444f4.png)
11. Trình bày các thành phần chính của nền tảng Apache Spark.
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
