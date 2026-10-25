# ffhibnese/Model-Inversion-Attack-ToolBox

⭐ 197 · Python · 推送 2026-09-15 · [GitHub](https://github.com/ffhibnese/Model-Inversion-Attack-ToolBox) · 组织维护

**模型反演攻击与防御的统一 Python 基准工具箱，面向隐私研究**

名为 MIA 的开源 Python 基准库，对 14 种模型反演攻击方法（DeepInversion、GMI、KEDMI、RLBMI 等，覆盖白盒/黑盒/label-only 场景）与 4 种防御方法（VIB、BiDO、TL、LS）做统一实现与封装，支持在同一框架下公平对比各方法；提供预训练目标模型与评估模型（Google Drive 发布）。运行环境为 Python 3.10、PyTorch 2.0.1、CUDA 11.8，通过 git clone + conda + pip 安装。由哈工大与清华相关研究者团队维护，配套综述论文被 IJCV 2026 接收。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 种攻击方法与 4 种防御方法的统一实现，覆盖白盒/黑盒/label-only 场景
- 提供预训练目标模型与评估模型文件
- 统一框架下对模型反演方法做公平对比

## 适用场景

- 在统一框架下复现与对比模型反演攻击方法
- 评估自己模型的隐私泄露风险并测试防御方法
- 模型反演方向论文研究的实验基线

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L18: Welcome to **MIA**! This repository is a comprehensive open-source Python benchmark for model inversion attacks, wh
> L26: **Model inversion attack** is an emerging powerful private data theft attack, where a malicious attacker is able to

## 星数曲线

```mermaid
xychart-beta
    title "ffhibnese/Model-Inversion-Attack-ToolBox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 196 --> 198
    line [197, 197]
```

2026-10-18 197 → 2026-10-25 197（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `f43fd237e035` · [字段定义](../../DATASET.md)*
