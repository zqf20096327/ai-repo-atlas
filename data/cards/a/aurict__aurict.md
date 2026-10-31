# aurict/aurict

⭐ 33 · TypeScript · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/aurict/aurict) · [官网](https://aurict.com/) · 组织维护

**终端原生 AI 编码 agent：多模型接入与沙箱化工具执行**

在终端中运行的 AI 编码助手：启动时扫描仓库（框架、语言、包管理器）注入上下文，通过类型化、权限控制的工具层执行文件读写、shell 命令与补丁应用，命令按安全/警告/危险三级分类并由策略沙箱约束。支持多 agent 并行编排（3+1 协调器模型）、218+ 技能、SQLite 会话记忆、上下文压缩与撤销。可接入 Anthropic/OpenAI/Google/OpenRouter/Ollama 等多种模型提供商，另提供 Flutter 移动端与 Web 平台。提供 npm 安装、一键安装脚本及源码编译（需 Bun 1.3+ 或 Node.js 20+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 策略沙箱与三级命令分类（safe/warning/danger），含审计日志与 GateGuard 保护
- 多 agent 并行编排：代码/审查/测试等专职 worker agent 与 3+1 协调器
- 218+ 技能按项目技术栈做结构化上下文注入
- 本地 HTTP API（JWT 认证）可从脚本或 CI 驱动会话

## 适用场景

- 在终端里让 AI 直接读写代码、执行命令并生成提交信息
- 通过子 agent 并行处理重构、写测试、安全审计等长任务
- 接入本地 Ollama 模型做离线编码辅助
- 从 CI 或脚本通过本地 API 驱动 agent 会话

## 场景标签

`编码 Agent` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A terminal-native AI coding assistant built for the way developers actually work.**
> L34: Aurict scans your repository on startup — framework, language, package manager, config files,
> L39: Every file read, shell command, and code edit happens through a typed, permission-controlled

## 星数曲线

```mermaid
xychart-beta
    title "aurict/aurict 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2cadfa40d68e` · [字段定义](../../DATASET.md)*
