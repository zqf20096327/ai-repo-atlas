# aovestdipaperino/laya-rust

⭐ 17 · Rust · Apache-2.0 · 推送 2026-09-30 · [GitHub](https://github.com/aovestdipaperino/laya-rust) · 个人维护

**Laya 类型化决策模型的纯 Rust 推理实现（candle）**

基于 candle 的 Rust 推理 crate，运行 Laya 非自回归类型化决策模型（ModernBERT-large + RL 决策头）：输入 state 与三类类型化问题（choice/score/noul），单次前向传播返回带校准概率的类型化答案，不生成文本。支持 CPU/Metal/CUDA 后端，提供 CLI、Web 控制台与 Rust 库三种使用形式。README 指出基座检查点在作者基准上接近随机水平，强结果属于微调变体，需自行重拟合温度后方可信任概率。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 非自回归类型化决策：一次前向传播返回全部问题答案
- 纯 Rust 实现，无 Python/torch/ONNX 导出步骤
- 支持 CPU/Metal/CUDA 后端，f32 与 f16 精度
- 提供 CLI、本地 Web 控制台（prompt inspector）与 Rust 库接口

## 适用场景

- 在 Rust 项目中以库形式集成类型化决策推理
- 本地运行 Laya 模型做支持工单分诊、内容审核等决策
- 通过 Web 控制台检查 prompt token 序列与答案概率分布

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Rust inference for Laya, a non-autoregressive
> L6: it a **state** (text or JSON) and a set of **typed questions**; it returns typed answers with
> L10: Pure Rust on candle — no Python, no torch, no ONNX

## 星数曲线

```mermaid
xychart-beta
    title "aovestdipaperino/laya-rust 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6c96ed411182` · [字段定义](../../DATASET.md)*
