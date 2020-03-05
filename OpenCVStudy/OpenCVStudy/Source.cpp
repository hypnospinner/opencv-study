#include<opencv2/opencv.hpp>
#include<iostream>

int main()
{
	cv::Mat img = cv::imread("lena.jpg");

	cv::namedWindow("image", cv::WINDOW_NORMAL);

	cv::imshow("image", img);

	cv::waitKey(0);

	return 0;
}