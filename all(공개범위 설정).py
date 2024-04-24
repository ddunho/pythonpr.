from travel import * #공개범위를 설정해야 오류가 안뜸(trip_to는 패키지로 되어있는 상태)
trip_to = vietnam.VietnamPackage()
trip_to.detail()

__all__ = ["vietnam,Thailand"] #공개범위 설정

trip_to =Thailand.ThailandPackage()
#정의되지않음 >> 공개범위 설정해야함 _all_에 추가


