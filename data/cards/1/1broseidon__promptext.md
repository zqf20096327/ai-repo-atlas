# 1broseidon/promptext

⭐ 22 · Go · MIT · 推送 2026-04-12 · [GitHub](https://github.com/1broseidon/promptext) · [官网](https://chain.sh/promptext) · 个人维护

**把代码库转成 AI 就绪提示词的 CLI/Go 库**

用 Go 编写的命令行工具（别名 prx），将项目代码过滤、按相关性评分排序并打包为面向 LLM 的 token 高效格式，支持 token 预算控制与 tiktoken（cl100k_base）计数。输出格式含 PTX、TOON-strict、Markdown、XML、JSONL，结果可复制到剪贴板粘贴给 Claude、ChatGPT 等。提供安装脚本、go install 与预编译二进制，也可作为 Go 库以 go get 方式集成，配置支持项目级 .promptext.yml 与全局配置文件。

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

- 关键词相关性评分（文件名/路径/导入/内容加权）筛选文件
- token 预算强制约束与 cl100k_base 准确计数
- 多种输出格式（PTX/TOON-strict/Markdown/XML/JSONL）
- 可作为 Go 库嵌入自有程序，支持丰富的函数式选项

## 适用场景

- 把整个项目打包给 Claude/ChatGPT 做代码审查或迁移
- 在有限上下文预算内聚焦与 bug 相关的文件做 AI 分析
- 以 Go API 将代码上下文提取集成进 AI/ML 工作流

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Convert your codebase into AI-ready prompts**
> L27: `promptext` intelligently filters your codebase, ranks files by relevance, and packages them into token-efficient f
> L115: - 🔌 **Library Integration** — Use the Go API to integrate code extraction into your AI/ML workflows

## 星数曲线

```mermaid
xychart-beta
    title "1broseidon/promptext 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2da0b2486cca` · [字段定义](../../DATASET.md)*
