{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "8d188a34",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "270365cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "img=np.zeros((600,1000,3),np.uint8)\n",
    "img1 = cv2.circle(img,(500,200),100, (0,255,255), 5)\n",
    "img1 = cv2.circle(img,(465,175),5, (0,255,255), 4)\n",
    "img1 = cv2.circle(img,(535,175),5, (0,255,255), 4)\n",
    "img1 = cv2.ellipse(img,(500,225),(50,15),0,0,180,(0,0,255),4)\n",
    "cv2.imshow(\"Simple_Face\",img1)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "9e2495f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "pic1 =cv2.imread(\"chota.jpg\")\n",
    "pic2 =cv2.imread(\"kaliya.jpg\")\n",
    "cv2.imshow(\"Chota_Beem\",pic1)\n",
    "cv2.imshow(\"Kaliya\",pic2)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "a4bb1de3",
   "metadata": {},
   "outputs": [],
   "source": [
    "beem_face=pic1[20:130,70:195]\n",
    "cv2.imshow(\"beem_frace\",beem_face)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()\n",
    "\n",
    "kaliya_face=pic2[20:130,70:195]\n",
    "cv2.imshow(\"kaliya_frace\",kaliya_face)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "6272b8d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "beem_face=pic1[20:130,70:195]\n",
    "pic2[20:130,70:195]=beem_face\n",
    "cv2.imshow(\"Swap_frace1\",pic2)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()\n",
    "\n",
    "kaliya_face=pic2[20:130,70:195]\n",
    "pic1[20:130,70:195]=kaliya_face\n",
    "cv2.imshow(\"Swap_frace2\",pic1)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "709d04e7",
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "def vconcat_resize(img_list, interpolation \n",
    "                   = cv2.INTER_CUBIC):\n",
    "      # take minimum width\n",
    "    w_min = min(img.shape[1] \n",
    "                for img in img_list)\n",
    "      \n",
    "    # resizing images\n",
    "    im_list_resize = [cv2.resize(img,\n",
    "                      (w_min, int(img.shape[0] * w_min / img.shape[1])),\n",
    "                                 interpolation = interpolation)\n",
    "                      for img in img_list]\n",
    "    # return final image\n",
    "    return cv2.vconcat(im_list_resize)\n",
    "  \n",
    "# function calling\n",
    "img_v_resize = vconcat_resize([pic1, pic2])\n",
    "  \n",
    "# show the output image\n",
    "cv2.imshow('vconcat_resize.jpg', img_v_resize)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dee7688b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
