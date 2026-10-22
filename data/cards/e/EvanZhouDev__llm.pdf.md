# EvanZhouDev/llm.pdf

⭐ 870 · Python · 推送 2026-09-13 · [GitHub](https://github.com/EvanZhouDev/llm.pdf) · [官网](http://evanzhoudev.github.io/llm.pdf) · 个人维护

**在 PDF 文件内运行 LLM 推理的概念验证项目**

概念验证项目，证明可在纯 PDF 文件中运行大语言模型推理。机制：用 Emscripten 将 llama.cpp 编译为 asm.js，通过旧的 PDF JS 注入执行，并把整个 LLM 模型以 base64 嵌入 PDF。提供 scripts/generatePDF.py 脚本，可将任意兼容的 GGUF 量化模型（建议 Q8）打包进 PDF；README 注明 135M 参数模型约 5 秒/token，更大模型会明显更慢。面向对 LLM 与 PDF 技术边界感兴趣的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Emscripten 将 llama.cpp 编译为 asm.js 并在 PDF 内运行
- 模型文件以 base64 完整嵌入 PDF
- generatePDF.py 支持打包任意 GGUF 量化模型
- README 标明 135M 参数模型约 5s/token 的性能参考

## 适用场景

- 把 GGUF 模型打包成可自包含运行的 PDF 做演示
- 验证 PDF JS 注入执行推理的技术可行性
- 作为 LLM 边缘部署方式的实验材料

## 场景标签

 · 领域:LLM 实验/概念验证

## 证据(README 行号)

> L7: This is a proof-of-concept project, showing that it's possible to run an entire Large Language Model in nothing but 
> L9: It uses Emscripten to compile llama.cpp into asm.js, which can then be run in the PDF using an old PDF JS injection.
> L11: Combined with embedding the entire LLM file into the PDF with base64, we are able to run LLM inference in nothing b

## 星数曲线

```mermaid
xychart-beta
    title "EvanZhouDev/llm.pdf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 869 --> 871
    line [870, 870]
```

2026-10-18 870 → 2026-10-22 870（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `68e907e644cc` · [字段定义](../../DATASET.md)*
