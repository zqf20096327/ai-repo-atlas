# hebo1221/nano-deepseek-v4

⭐ 20 · Python · Apache-2.0 · 推送 2026-08-14 · [GitHub](https://github.com/hebo1221/nano-deepseek-v4) · [官网](https://github.com/hebo1221/nano-deepseek-v4#readme) · 个人维护

**DeepSeek-V4 架构的可读 PyTorch 参考实现与 CPU 一致性验证套件**

仿照 nanoGPT 风格、约 4,300 行代码的 DeepSeek-V4（Flash/Pro）架构参考实现：在 modeling.py 中以可读的 PyTorch 方程实现滑动注意力、CSA、HCA、mHC、MoE 路由、Lightning Indexer 与 MTP 等模块，并提供 CPU 可运行的一致性 profile、DSpark 方程与调度检查器、小型可复现训练/生成工具及官方 checkpoint 检查器。定位为参考与一致性验证面，不是生产训练或推理框架；物化 284B/1.6T 模型仍需大内存。通过 PyPI 或源码安装，要求 Python 3.10+ 与 PyTorch 2.4+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可读 PyTorch 方程实现 DeepSeek-V4 架构（CSA/HCA/mHC/MoE/MTP 等）
- 无下载的 CPU demo、guided tour 与一致性 profile（core/dspark/offline/live）
- 带确定性 JSON 回执的固定复现训练与小模型生成
- 官方 checkpoint 元数据/shard 头部检查器

## 适用场景

- 阅读并理解 DeepSeek-V4 架构的各模块张量流程
- 在 CPU 上验证架构实现与固定向量/参考实现的 一致性
- 跑小型可复现训练与生成，学习整合 checkpoint bundle 流程

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L9: A CPU-runnable conformance and reference lab for the **DeepSeek-V4**
> L15: The native model follows the

## 星数曲线

```mermaid
xychart-beta
    title "hebo1221/nano-deepseek-v4 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6c2773f6f5d6` · [字段定义](../../DATASET.md)*
