# videlalvaro/emilio

⭐ 24 · Python · MIT · 推送 2026-04-26 · [GitHub](https://github.com/videlalvaro/emilio) · 个人维护

**用单一 EML 代数原语实现 LLM 推理的 Rust 引擎**

基于 Odrzywołek (2026) 的 EML 原语 eml(x,y)=exp(x)−ln(y) 构建的 LLM 推理引擎：以 exp(ln(a)+ln(b)) 表达全部乘法运算，完成 Qwen2.5-0.5B-Instruct 的完整前向传播，在 Apple Silicon 上 CPU 约 5.5 tok/s、Metal GPU 约 30 tok/s。提供 Rust 引擎（CPU+Metal）、Python 验证脚本、GGUF→.eml 编译器与论文。README 声明目标为验证代数恒等式而非追求推理速度（建议追求速度者使用 llama.cpp），需 Rust≥1.75、macOS Apple Silicon 支持 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 前向传播中每次乘法均通过 exp(ln(a)+ln(b)) 实现（636K EML 调用/token）
- Rust 引擎支持 CPU 与 Metal GPU（4 个纯 EML 核）
- GGUF→.eml 编译格式在编译期预计算 ln(W)
- 提供 Python 与 Rust 的正确性验证脚本及配套论文

## 适用场景

- 研究单一代数原语表达完整 transformer 的可行性
- 在 Apple Silicon 上运行经 EML 变换的 Qwen 0.5B 模型
- 复现论文中的优化层级与核基准测试

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L13: this by running Qwen2.5-0.5B-Instruct (494M parameters) entirely through EML, producing
> L24: |`emilio/`|**emilio** — Rust inference engine (CPU + Metal GPU)|

## 星数曲线

```mermaid
xychart-beta
    title "videlalvaro/emilio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-28 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `2906ffe7a152` · [字段定义](../../DATASET.md)*
