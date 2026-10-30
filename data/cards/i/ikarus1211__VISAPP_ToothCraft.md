# ikarus1211/VISAPP_ToothCraft

⭐ 16 · Python · AGPL-3.0 · 推送 2026-10-13 · [GitHub](https://github.com/ikarus1211/VISAPP_ToothCraft) · 组织维护

**基于扩散模型的 3D 牙冠补全方法（科研代码）**

ToothCraft 是基于符号距离函数（SDF）扩散模型的学习型 3D 牙冠补全方法：从部分缺失或损坏的牙冠几何出发，利用邻牙与牙弓局部形态作为条件上下文，生成完整牙冠形状，覆盖不同牙位与多种损伤程度。附带合成训练数据生成管线（AugmentPipeline）。面向牙科修复工作流的研究人员与开发者。安装需克隆仓库、Conda 环境（Python 3.10）、PyTorch 2.9.0 与 requirements.txt 依赖，通过 hydra 配置训练与测试，预训练权重托管于 Hugging Face。软件采用 AGPL-3.0 双许可条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SDF 上的扩散模型生成完整牙冠形状
- 以邻牙/牙弓局部几何为条件，保留形态与咬合面
- 附带从完整牙弓构建合成训练样本的数据生成管线
- 预训练 checkpoint 发布于 Hugging Face

## 适用场景

- 从部分几何补全缺失或受损的牙冠
- 生成可用于牙科修复工作流的患牙专属牙冠形状
- 构建合成 SDF 训练数据集复现研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L18:  ToothCraft is a learning-based 3D tooth crown completion method built on diffusion models over Signed Distance Fun
> L20: ToothCraft reconstructs missing or damaged tooth crowns from partial geometry while using the surrounding dental ar
> L27: - Diffusion-based generation on Signed Distance Functions (SDFs).

## 星数曲线

```mermaid
xychart-beta
    title "ikarus1211/VISAPP_ToothCraft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `cb4cb2b9f810` · [字段定义](../../DATASET.md)*
