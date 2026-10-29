# kyegomez/ScreenAI

⭐ 387 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/kyegomez/ScreenAI) · [官网](https://discord.gg/GYbXvDGevY) · 个人维护

**ScreenAI 视觉语言模型的 PyTorch 复现：UI 与信息图理解**

论文《ScreenAI: A Vision-Language Model for UI and Infographics Understanding》的第三方实现：输入图像与文本，经 patch 化、ViT 编码、注意力与前馈层及交叉注意力，输出模型前向结果。以 Python 包形式提供，pip 安装后可 import ScreenAI 使用。README 的 Todo 部分列有尚未完成的项目（如编码器/解码器中的 nn.ModuleList 实现），表明实现仍在开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 复现 ScreenAI 视觉语言模型架构（ViT + 交叉注意力）
- pip 安装，PyTorch 代码示例演示用法
- 提供论文引用（arXiv 2409.03977）

## 适用场景

- 在 UI 截图与信息图理解任务上运行 ScreenAI 模型
- 研究视觉语言模型架构实现细节

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L4: Implementation of the ScreenAI model from the paper: "A Vision-Language Model for UI and Infographics Understanding"
> L14: from screenai.main import ScreenAI

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/ScreenAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 386 --> 388
    line [387, 387]
```

2026-10-18 387 → 2026-10-29 387（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8926ebeae2b8` · [字段定义](../../DATASET.md)*
