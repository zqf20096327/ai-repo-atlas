# takashiishida/arxiv-to-prompt

⭐ 170 · Python · MIT · 推送 2026-08-24 · [GitHub](https://github.com/takashiishida/arxiv-to-prompt) · 个人维护

**把 arXiv 论文转成单一 LaTeX 源供向 LLM 提问的命令行工具**

命令行工具：下载 arXiv 论文源文件，自动定位含 \documentclass 的主 tex 文件，解析 \input/\include 将多文件扁平化为单一 LaTeX 源，可选去除注释与附录以缩短 prompt；支持 arXiv ID 或 URL 输入，本地缓存避免重复下载，并提供 Python API（process_latex_source）。面向需要把论文全文喂给 LLM 做问答的研究者与开发者，README 列出 MCP server、论文转 slides 等下游项目。

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

- 自动识别主 tex 文件并解析 \input/\include 扁平化为单一源
- 可选移除 LaTeX 注释与附录以缩短 prompt
- 本地缓存下载的论文，支持强制重新下载
- 提供 CLI 与 Python API 两种使用方式

## 适用场景

- 把论文 LaTeX 源整理成 prompt，向 LLM 提问论文细节
- 批量提取 arXiv 论文源文件供下游工具（MCP、转 slides）使用
- 去掉注释和附录以控制输入长度

## 场景标签

 · 领域:LLM 工具/学术

## 证据(README 行号)

> L7: A command-line tool to transform arXiv papers into a single LaTeX source that can be used as a prompt for asking LLM
> L37: You can also use arxiv-to-prompt in your Python code:

## 星数曲线

```mermaid
xychart-beta
    title "takashiishida/arxiv-to-prompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 169 --> 171
    line [170, 170]
```

2026-10-18 170 → 2026-10-23 170（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d24d6362addb` · [字段定义](../../DATASET.md)*
