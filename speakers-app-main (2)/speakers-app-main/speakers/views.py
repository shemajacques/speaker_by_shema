from django.shortcuts import render

# Create your views here.

speakers = [
    {
        "id": 1,
        "name": "Grace Hopper",
        "profession": "Fashion Designer",
        "image": "https://images.pexels.com/photos/4420634/pexels-photo-4420634.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "bio": "Lorem ipsum dolor sit amet",
    },
    {
        "id": 2,
        "name": "Monstrea Khan",
        "profession": "Computer Scientist",
        "image": "https://images.pexels.com/photos/5384445/pexels-photo-5384445.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "bio": "Lorem ipsum dolor sit amet",
    },
    {
        "id": 3,
        "name": "Brad Philip",
        "profession": "Real Estate Agent",
        "image": "https://images.pexels.com/photos/5490276/pexels-photo-5490276.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "bio": "Lorem ipsum dolor sit amet",
    },
    {
        "id": 4,
        "name": "Sara Smith",
        "profession": "HR Manager",
        "image": "https://images.pexels.com/photos/5876695/pexels-photo-5876695.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "bio": "Lorem ipsum dolor sit amet",
    },
    {
        "id": 5,
        "name": "Chris Jonas",
        "profession": "Graphic Designer",
        "image": "https://images.pexels.com/photos/5792641/pexels-photo-5792641.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "bio": "Lorem ipsum dolor sit amet",
    },
    {
        "id": 6,
        "name": "Achraf Yousfi",
        "profession": "Banker",
        "image": "https://images.pexels.com/photos/5378700/pexels-photo-5378700.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "bio": "Lorem ipsum dolor sit amet",
    },
]


def speakers_list(request):
    return render(request, "speakers_list.html", {"speakers": speakers})


def speaker_detail(request, pk: int):
    try:
        speaker = list(filter(lambda speaker: speaker["id"] == pk, speakers))[0]
        return render(request, "speaker_detail.html", {"speaker": speaker})
    except IndexError:
        return render(request, "speaker_not_found.html")


def speaker_update(request, pk: int):
    try:
        speaker = list(filter(lambda speaker: speaker["id"] == pk, speakers))[0]
        return render(request, "speaker_update.html", {"speaker": speaker})
    except IndexError:
        return render(request, "speaker_not_found.html")

def speaker_delete(request, pk: int):
    try:
        speaker = list(filter(lambda speaker: speaker["id"] == pk, speakers))[0]
        return render(request, "speaker_delete.html", {"speaker": speaker})
    except IndexError:
        return render(request, "speaker_not_found.html")
