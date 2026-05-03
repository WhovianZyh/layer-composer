# Layer Composer

A web-based tool for composing layered transparent PNGs into a single image. Drag, toggle, reorder layers, and export the result as a PNG.

一个网页工具，将分层透明 PNG 素材叠加合成为一张图。支持拖拽排序、显示/隐藏图层、实时预览、一键导出。

## Quick Start / 快速开始

```bash
git clone https://github.com/WhovianZyh/layer-composer.git
cd layer-composer
python3 server.py
# Open http://localhost:8080
```

Zero dependencies — Python 3 standard library only. / 零依赖，仅需 Python 3 标准库。

## Project Structure / 项目结构

```
layer-composer/
├── server.py          # HTTP server & API / HTTP 服务及接口
├── index.html         # Web UI / 网页界面
└── my-character/      # Your asset folder / 你的素材文件夹（自行创建）
    ├── body.png
    ├── head_normal.png
    ├── head_smile.png
    ├── clothes.png
    ├── blush.png
    └── ...
```

Place each set of PNG layers in its own subdirectory. All PNGs in a single folder should share the same canvas dimensions — they will be stacked pixel-perfect. Transparent PNGs are expected.

将每组 PNG 素材放入各自的子文件夹。同一文件夹内的 PNG 应当画布尺寸一致，这样才能像素级对齐叠加。素材应为透明背景 PNG。

## Features / 功能

| | |
|---|---|
| **Layer toggling** / 图层开关 | Check/uncheck layers in the grid |
| **Drag and drop** / 拖拽排序 | Drag thumbnails to reorder layers |
| **Arrow buttons** / 箭头微调 | Fine-tune layer order with ▲ ▼ buttons |
| **Real-time preview** / 实时预览 | Canvas updates instantly on every change |
| **Auto-sort** / 自动排序 | Layers ordered by opaque pixel count (larger → bottom) |
| **Export PNG** / 导出 | Download the final composition as a single PNG |
| **i18n** / 双语 | English / Chinese language toggle |
| **Reset order** / 重置 | One-click restore to default ordering |

## Custom Port / 自定义端口

```bash
python3 server.py 9090
```
