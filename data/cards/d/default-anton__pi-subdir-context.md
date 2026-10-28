# default-anton/pi-subdir-context

⭐ 35 · TypeScript · MIT · 推送 2026-08-06 · [GitHub](https://github.com/default-anton/pi-subdir-context) · 个人维护

**pi 编码代理扩展：自动注入子目录 AGENTS/CLAUDE 上下文**

面向 pi coding agent 的扩展：当用户使用 read 工具读取文件时，沿目录树向上查找 AGENTS.override.md、AGENTS.md 或 CLAUDE.md 上下文文件，按离文件由近到远的顺序注入工具结果中；同一目录下 override 文件优先，已加载文件按会话去重。查找止于项目根目录，项目外与家目录外文件被忽略。通过 pi install npm:pi-subdir-context 安装，或用 pi -e 临时试用，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- read 文件时自动发现并注入路径层级中的 AGENTS/CLAUDE 上下文
- AGENTS.override.md 与 CLAUDE.md、AGENTS.md 三种文件名支持与优先级规则
- 按会话去重，查找范围止于项目根目录

## 适用场景

- 在 monorepo 子目录中让代理自动获得局部规则上下文
- 复用已有 CLAUDE.md 项目规则而无需手动加载
- 为不同模块维护不同的代理行为说明

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Automatically load `AGENTS` or `CLAUDE` context (`AGENTS.override.md`, `AGENTS.md`, or `CLAUDE.md`) from subdirector
> L7: When you read a file in a subdirectory (e.g., `src/components/Button.tsx`), this extension automatically discovers a
> L23: 1. When you use the `read` tool, the extension checks the file's directory path

## 星数曲线

```mermaid
xychart-beta
    title "default-anton/pi-subdir-context 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f0fb4da0beaf` · [字段定义](../../DATASET.md)*
