# ali-faraz-py/deepfake-detector

⭐ 34 · JavaScript · 推送 2026-08-17 · [GitHub](https://github.com/ali-faraz-py/deepfake-detector) · [官网](https://deepfake-detector-olive.vercel.app) · 个人维护

**全栈 Web 应用：上传人脸图像/视频，判定 Real 或 Fake 并给出置信度**

个人全栈作品：前端 Next.js 部署于 Vercel，后端 FastAPI 部署于 Render，模型为 PyTorch EfficientNet-B0，在 Kaggle 140k Real and Fake Faces 数据集上训练（10 万训练图，~99.7% 训练准确率）。图像直接分类，视频用 OpenCV 抽样 5-10 帧分别判定后取平均。README 明示局限：训练分布为 StyleGAN 生成的人脸，对扩散模型（如 Midjourney）生成的图像可能不可靠；免费托管导致冷启动 30-60 秒。本地运行需分别安装后端与前端依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图像/视频上传分类为 Real/Fake 并返回置信度
- 视频抽样多帧取平均预测
- EfficientNet-B0，训练于 10 万张图像数据集
- 界面含拖拽上传、历史记录、示例按钮与泛化局限免责声明

## 适用场景

- 核验一张人脸图像是否为 AI 生成
- 上传短视频获得真伪判定与置信度
- 作为计算机视觉+全栈部署的学习/作品参考

## 场景标签

`人脸识别` `网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: An AI-powered web app that analyzes uploaded face images and videos to classify them as **Real** or **Deepfake**, wi
> L15: - The model classifies it as **Real** or **Fake**

## 星数曲线

```mermaid
xychart-beta
    title "ali-faraz-py/deepfake-detector 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-28 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0db9173da4dd` · [字段定义](../../DATASET.md)*
