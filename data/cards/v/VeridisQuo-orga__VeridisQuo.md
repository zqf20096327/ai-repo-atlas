# VeridisQuo-orga/VeridisQuo

⭐ 67 · Python · Apache-2.0 · 推送 2026-01-08 · [GitHub](https://github.com/VeridisQuo-orga/VeridisQuo) · [官网](https://huggingface.co/spaces/Gazeux33/veridisquo-deepfake-detection) · 组织维护

**检测深伪视频并标注篡改区域的可解释深度学习模型**

混合架构（空间流 EfficientNet-B4 + 频率流）的深伪视频检测模型与应用：输入 224×224 人脸图像，输出 FAKE/REAL 二分类与置信度，并用 GradCAM 生成篡改区域可视化。模型在 FaceForensics++ (C23) 预处理后数据集（716,438 张图像）上训练，参数量 25.05M。提供 FastAPI 后端（视频上传、逐帧分析、分数聚合、可视化下载）与 Node.js 前端，通过 git clone 与脚本启动，另有 HuggingFace 在线演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 空间+频率双流混合检测架构，输出二分类结果与置信度
- GradCAM 可解释性可视化，标注每帧被篡改区域
- REST API 支持上传 MP4/AVI/MOV/MKV/WEBM 视频并逐帧分析
- 在 FaceForensics++ (C23) 派生的 716,438 张图像数据集上训练

## 适用场景

- 上传视频检测是否为深伪并查看篡改区域热图
- 通过 API 集成深伪检测到自己的应用
- 复现训练流程或使用预训练模型做研究实验

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7: A state-of-the-art neural network designed to **detect deepfake videos** and **highlight the altered areas** in each
> L44: |**Output**|Binary (FAKE/REAL) + confidence|

## 星数曲线

```mermaid
xychart-beta
    title "VeridisQuo-orga/VeridisQuo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-26 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3e9caaa300e3` · [字段定义](../../DATASET.md)*
