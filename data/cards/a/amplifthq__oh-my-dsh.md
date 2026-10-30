# amplifthq/oh-my-dsh

⭐ 16 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/amplifthq/oh-my-dsh) · [官网](https://www.npmjs.com/package/oh-my-dsh) · 组织维护 · 中文 README

**DeepSeek Harness 的精选发行版：开箱即用的编码智能体环境**

在 DeepSeek Harness 之上叠加的 curated distribution（Overlay 而非 fork）：提供交互式 Web UI 与 headless 两个隔离 profile、SSRF 加固的默认 web fetch、LSP 导航与可预览/可回滚的语义重命名、惰性 MCP 能力控制（编目不启动、激活需审批）、沿用既有 AGENTS.md/Claude/Cursor/Codex 配置、插件目录与审批门控的技能蒸馏。锁定已测试的上游版本，保留'一切皆插件'架构且每个选择可覆盖。面向开发者与终端用户双渠道：便携版内嵌 Node.js 运行时（macOS arm64/Linux x64 glibc，原生 Windows 不支持，需 WSL2），npm 面向开发者组合。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Overlay 形式叠加 DeepSeek Harness，锁定已测试上游版本而非跟随破坏性变更
- 惰性 MCP 控制：编目不启动进程、不注入工具 schema，激活需 proposal_control 审批
- 内置多语言 LSP 与带审批/回滚/恢复日志的语义重命名
- 原位读取既有 AGENTS.md/Claude/Cursor/Codex 指令、技能与 MCP 配置

## 适用场景

- 获得一个预设好权限与默认值的编码智能体工作环境
- 在 Windows/macOS/Linux 上免系统 Node.js 快速安装并运行 DeepSeek Harness
- 复用我现有的 Claude/Cursor/Codex 配置与 MCP 服务器
- 对 MCP 服务器与插件做审批式的细粒度启用控制

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: DeepSeek Harness provides an excellent plugin framework and a conservative reference setup. `oh-my-dsh` turns those
> L16: It is a native curated distribution, not a fork. You keep upstream's “everything is a plugin” architecture and can 
> L18: > DeepSeek Harness is in developer preview. `oh-my-dsh` pins a tested upstream release instead of silently followin

## 星数曲线

```mermaid
xychart-beta
    title "amplifthq/oh-my-dsh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `912082cb5485` · [字段定义](../../DATASET.md)*
