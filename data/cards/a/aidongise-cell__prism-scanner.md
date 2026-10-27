# aidongise-cell/prism-scanner

⭐ 28 · Python · Apache-2.0 · 推送 2026-04-07 · [GitHub](https://github.com/aidongise-cell/prism-scanner) · [官网](https://github.com/aidongise-cell/prism-scanner#-prism-scanner) · 组织维护

**AI Agent 技能/插件/MCP 服务器的安全扫描器**

纯静态分析的本地安全扫描 CLI，覆盖安装前代码审查与卸载后残留检测：14 条代码行为规则（shell 执行、数据外传、SSRF、持久化等）、15 条元数据/发布卫生规则（硬编码凭证、typosquatting、提示注入、心理操纵模式等）、10 条系统残留规则（LaunchAgents、crontab、shell 配置污染等），共 39 条检测规则与轻量文件内污点分析。支持 ClawHub 技能、MCP 服务器、npm/pip 包多平台，输出 A–F 评级、HTML 报告，可作 MCP Server、GitHub Action 或 Docker 运行，并支持三段式安全清理与回滚。面向在安装 agent 技能前做安全把关、或在 CI 中拦截高危发现的开发者与团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3 层 39 条检测规则：代码行为（S）、元数据/发布卫生（M/P）、系统残留（R）
- 纯静态分析，不执行被扫描代码，支持 --offline 离线运行
- 可运行于 CLI、MCP Server（暴露 4 个工具）、GitHub Action 与 Docker
- YAML 规则文件可扩展，.prismignore 支持带理由的抑制

## 适用场景

- 安装第三方 agent 技能或 MCP 服务器前扫描恶意行为
- 卸载工具后检测系统中的持久化残留与凭证泄漏
- 在 CI 流水线中按严重级别阻断不安全发布
- 为通过扫描的项目展示 Prism 评级徽章

## 场景标签

`代码审查` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L9: **Security scanner for AI Agent skills, plugins, and MCP servers.**
> L72: Prism Scanner can run as an MCP server, giving AI assistants direct access to security scanning tools.
> L119: **Total: 39 detection rules** with lightweight intra-file taint analysis.

## 星数曲线

```mermaid
xychart-beta
    title "aidongise-cell/prism-scanner 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-27 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e62a094434cf` · [字段定义](../../DATASET.md)*
