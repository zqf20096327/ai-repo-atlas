# georgebuilds/anneal

⭐ 33 · Go · AGPL-3.0 · 推送 2026-06-26 · [GitHub](https://github.com/georgebuilds/anneal) · [官网](https://georgebuilds.github.io/anneal/) · 个人维护

**Go 编写的张量编译器：tinygrad 核心的从零移植**

用 Go 从零移植 tinygrad rangeify 时代核心的研究型机器学习编译器：前向、梯度与 movement 操作统一为不可变 UOp IR 节点，autodiff 作为图重写 pass 注入同一图，调度器跨前向/反向边界融合内核；movement 操作转为索引算术不复制数据。后端为零 CGO 的 WebGPU（原生 + WASM）与纯 Go CPU 解释器，支持 ONNX 1.17 纯 Go 导入（约 100 个算子）、符号形状、JIT，可端到端训练 MLP、nanoGPT、Llama 式解码器等并微调 GPT-2-small。附带单二进制本地浏览器 studio（8 个视图，零遥测）。README 自述为研究项目，非生产框架的即插替代。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- autodiff 作为图重写 pass，调度器跨前向/反向边界融合内核
- 零 CGO WebGPU 后端（原生 + WASM），同一编译器构建浏览器可视化
- 纯 Go protobuf 绑定导入 ONNX 1.17 模型（约 100 个算子）
- 单二进制本地浏览器 studio：8 个深度链接视图，模型字节不离开本机

## 适用场景

- 在 Go 中以编译器方式构建和训练小型神经网络模型
- 导入并可视化 ONNX 模型拓扑与生成的 WGSL 内核
- 在浏览器中通过 WASM 运行真实编译器进行学习与实验

## 场景标签

`模型训练` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: **A tensor compiler in Go. Autodiff is a graph rewrite, kernels fuse across the forward/backward seam, ONNX import i
> L15: anneal is a from-scratch Go port of tinygrad's modern, *rangeify-era* core. It takes tensor programs, lowers them t
> L23: - **It's a compiler, not an autodiff library.** Everything (forward ops, gradients, movement ops) is a single immut

## 星数曲线

```mermaid
xychart-beta
    title "georgebuilds/anneal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ffb9225c2a83` · [字段定义](../../DATASET.md)*
