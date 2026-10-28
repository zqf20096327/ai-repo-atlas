# suxrobGM/bookshelf-scanner

⭐ 21 · Python · MIT · 推送 2026-03-20 · [GitHub](https://github.com/suxrobGM/bookshelf-scanner) · 个人维护

**从书架照片识别书籍名称与作者的 Web 应用（YOLO+Moondream2）**

端到端的三组件应用：Python AI 服务用 YOLO 11x 分割模型从书架图片中切出书脊，再用微调量化过的 Moondream2 LLM 识别每本书的标题与作者；FastAPI 后端提供 POST /api/predict 接口，先返回 base64 分割图，再流式推送识别结果；Angular+Bun 前端负责上传与实时展示。图像预处理含缩放至 2560 像素、增强对比亮度与去噪。运行需 Bun、Python 3.12、Poetry 与 CUDA Toolkit 12.4+，前后端需分别手动启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLO 11x 分割模型从书架图片提取书脊并裁剪旋转
- 微调量化的 Moondream2 LLM 识别书名与作者
- FastAPI 流式接口：先返回分割图，再增量推送识别结果
- Angular+Bun 前端实时展示流式识别数据

## 适用场景

- 上传书架照片批量获取书名与作者清单
- 个人藏书数字化整理

## 场景标签

 · 领域:计算机视觉/图像识别应用

## 证据(README 行号)

> L3: The Bookshelf Scanner App is an end-to-end solution for detecting books from an image of a bookshelf and identifying
> L11:  - **LLM Inference (Moondream2):** After segmentation, the AI model uses a Moondream2 LLM to extract the book title
> L45: 5. **Recognition:** Each cropped book individual image is sent to the Moondream2 LLM model for title and author rec

## 星数曲线

```mermaid
xychart-beta
    title "suxrobGM/bookshelf-scanner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ad566cda0a47` · [字段定义](../../DATASET.md)*
