# raphaelmansuy/code2prompt

⭐ — · [GitHub]() · 个人维护

**把代码库转换成 LLM 可用 Markdown 提示词的命令行工具**

面向开发者的 Python 命令行工具：读取代码库文件，生成包含源码树与代码内容的 Markdown 提示词，供提交给大语言模型做代码分析、文档与改进任务。机制上支持 Jinja2 自定义模板与模板变量、glob 过滤/排除、.gitignore 集成、token 计数（默认 cl100k_base 编码）、行号标注、剪贴板复制与输出文件。限制：本工具自身不调用模型，仅生成提示词，需配合外部 LLM 使用。通过 pip/pipx 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将整个代码库生成结构化 Markdown 提示词（含源码树）
- Jinja2 模板定制输出，支持模板导入与输入变量
- glob 过滤/排除、.gitignore 集成与 token 计数
- 支持 --syntax-map 自定义扩展名语法高亮映射

## 适用场景

- 把项目代码打包成提示词交给 LLM 做代码分析或审查
- 为 AI 辅助文档生成准备代码上下文
- 统计并控制提示词 token 数以适配模型上下文限制

## 场景标签

 · 领域:开发者工具/LLM 上下文准备

## 证据(README 行号)

> L11: Code2Prompt is a powerful command-line tool that generates comprehensive prompts from codebases, designed to stream
> L23: Code2Prompt is a powerful, open-source command-line tool that bridges the gap between your codebase and Large Langu

## 星数曲线

```mermaid
xychart-beta
    title "raphaelmansuy/code2prompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 884 --> 886
    line [885, 885]
```

2026-10-18 885 → 2026-10-21 885（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `fbb9d5cd3b7a` · [字段定义](../../DATASET.md)*
