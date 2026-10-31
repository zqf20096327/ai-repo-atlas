# alessioarzenton/claude-code-wp-toolkit

⭐ 26 · Shell · GPL-3.0 · 推送 2026-02-23 · [GitHub](https://github.com/alessioarzenton/claude-code-wp-toolkit) · 个人维护

**为 WordPress 项目生成 Claude Code 配置的脚手架工具包**

面向 WordPress 开发者的 Claude Code 配置生成器：一个交互式 Bash 脚本根据项目技术栈（Bedrock 或标准 WordPress、Sage 或 Classic PHP 主题、ACF 配置）生成完整 .claude/ 目录，含技能、斜杠命令、子代理、钩子与文档。技能覆盖 Sage/Blade/Tailwind 4 约定、WCAG 2.2 AA 可访问性、REST API、插件开发等；钩子提供危险命令拦截、密钥检测与自动格式化；支持 Figma MCP 的设计转代码流程。通过 git clone 安装，需已装 Claude Code 与 Bash 3.2+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按技术栈（Bedrock/标准、Sage/Classic、ACF）生成分化配置
- WCAG 2.2 AA 可访问性规则与专用审计命令
- 安全钩子：危险 Bash 命令拦截、提交前密钥检测、权限拒绝清单
- Figma MCP 设计转代码斜杠命令与子代理

## 适用场景

- 为 Bedrock 或标准 WordPress 项目初始化 Claude Code 配置
- 让 Claude Code 按 Sage/Blade/Tailwind 4 项目约定生成代码
- 在 WP 开发流程中执行可访问性审计与安全检查

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L19: Claude WP Kit generates a complete `.claude/` configuration directory tailored to your WordPress project. It provid
> L25: - **Smart scaffolding** — One interactive script generates a full `.claude/` config customized for your project's s
> L175: │   └── init.sh                       # Interactive CLI installer (v1.0.0)

## 星数曲线

```mermaid
xychart-beta
    title "alessioarzenton/claude-code-wp-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c63c6fd845a6` · [字段定义](../../DATASET.md)*
