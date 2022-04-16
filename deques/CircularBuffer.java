package net.sophiale.deques;

import java.util.ArrayList;
import java.util.List;

public class CircularBuffer<T> {
    int mSize;
    int mFront;
    int mRear;
    int mBufLen;
    T[] mBuf;

    public CircularBuffer(int size) {
        mSize = size;
        mFront = 0;
        mRear = 0;
        mBufLen = 0;
        mBuf = new T[mSize];
    }

    public boolean enqueue(T value) {
        if (isFull()) {
            return false;
        }
        mRear = (mRear + 1) % mSize;
        mBuf[mRear] = value;
        mBufLen++;
        return true;
    }

    public T dequeue() {
        if (isEmpty()) {
            return null;
        }

        T value = mBuf[mFront];
        mFront = (mFront + 1) % mSize;
        mBufLen--;
        return value;
    }

    public T front() {
        return mBuf[mFront];
    }

    public int size() {
        return mBufLen;
    }

    public boolean isEmpty() {
        return (size() == 0);
    }

    public boolean isFull() {
        return (size() == mSize);
    }

    public String toString() {
        if (isEmpty()) {
            return "";
        }
        int start = mFront;
        StringBuilder builder = new StringBuilder();
        int i = start;
        while (mBuf[i] != null) {
            builder.append(mBuf[i].toString());
            builder.append(',');
            i = (i + 1) % mSize;
        }
        builder.setLength(builder.length() - 1);
        return builder.toString();
    }
}
