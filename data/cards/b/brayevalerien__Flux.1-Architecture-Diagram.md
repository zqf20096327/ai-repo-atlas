# brayevalerien/Flux.1-Architecture-Diagram

⭐ 87 · Typst · MIT · 推送 2026-10-19 · [GitHub](https://github.com/brayevalerien/Flux.1-Architecture-Diagram) · 个人维护

**Flux.1 [dev] 模型架构的详细图解（分解到单个 ML 模块）**

用 Typst 与 CeTZ 绘制的 Flux.1 [dev] 文生图模型架构图，将 Black Forest Labs 公开的 Flux 实现分解到单个机器学习模块。图中标注 19 个 DoubleStream 块、38 个 SingleStream 块、vec 调制向量构成、guidance 蒸馏、T5 提示固定填充 512 token、RoPE 三轴旋转、latent 通道打包与采样调度偏移等细节。每个图形有独立源文件，可用 typst compile 命令重建；另有 draw.io 初稿保留。适合阅读或讲解 Flux.1 结构的开发者与研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Typst+CeTZ 绘制，每个图形独立源文件，可命令行重编译
- 架构分解到单个 ML 模块（DoubleStream/SingleStream 块等）
- 附带 padding、RoPE 轴、latent 缩放系数等实现细节标注

## 适用场景

- 阅读理解 Flux.1 [dev] 的内部架构与各模块连接方式
- 讲解或学习 MMDiT 类文生图模型结构时用作参考图
- 基于图示定位实现细节（如 RoPE 维度、latent 打包方式）

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L2: A detailed diagram laying out the full Flux.1 [dev] architecture as shared by Black Forest Labs, broken down to sing
> L7: The diagram is written in Typst with CeTZ, every figure has its own file in `diagram/`. To rebuild it:

## 星数曲线

```mermaid
xychart-beta
    title "brayevalerien/Flux.1-Architecture-Diagram 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-28"]
    y-axis "stars" 86 --> 88
    line [87, 87]
```

2026-10-19 87 → 2026-10-28 87（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `79b5508919fd` · [字段定义](../../DATASET.md)*
