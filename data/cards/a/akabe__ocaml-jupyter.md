# akabe/ocaml-jupyter

⭐ 319 · Jupyter Notebook · MIT · 推送 2026-03-12 · [GitHub](https://github.com/akabe/ocaml-jupyter) · [官网](https://akabe.github.io/ocaml-jupyter/) · 个人维护

**面向 Jupyter 的 OCaml 内核：在笔记本中提供 OCaml REPL**

OCaml Jupyter 是一个 Jupyter notebook 内核，将 OCaml REPL 接入 Jupyter 交互环境，支持 Markdown/HTML 文档、MathJax 公式与图片嵌入显示。内核基于 merlin 提供代码补全与标识符检查，含 jupyter.notebook、jupyter.comm 子包用于控制 notebook 与前后端通信。通过 OPAM 安装并注册 kernelspec，需系统级依赖 zlib、libffi、libgmp、libzmq 5+；可在 Binder 与 Google Colab 上运行，支持 nbconvert 导出 HTML/Markdown/LaTeX。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 merlin 的 Tab 代码补全与 Shift+Tab 检查
- Markdown/HTML 文档、LaTeX 公式与图片嵌入
- jupyter.notebook / jupyter.comm 子包支持动态生成与前后端通信
- 支持 Binder 与 Google Colab 运行环境

## 适用场景

- 在 Jupyter 中交互式编写与运行 OCaml 代码
- 用 notebook 形式做 OCaml 数据分析与教学
- 将 OCaml notebook 通过 nbconvert 导出为 HTML/LaTeX/.ml 文件

## 场景标签

 · 领域:编程语言工具/Jupyter 生态

## 证据(README 行号)

> L6: An OCaml kernel for [Jupyter notebook][jupyter].
> L8: This provides an OCaml REPL with a great user interface such as markdown/HTML documentation, LaTeX formula by MathJa

## 星数曲线

```mermaid
xychart-beta
    title "akabe/ocaml-jupyter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 318 --> 320
    line [319, 319]
```

2026-10-18 319 → 2026-10-24 319（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `3954aa75fe04` · [字段定义](../../DATASET.md)*
