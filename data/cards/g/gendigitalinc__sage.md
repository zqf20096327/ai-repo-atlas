# gendigitalinc/sage

⭐ 319 · TypeScript · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/gendigitalinc/sage) · [官网](https://ai.gendigital.com/sage) · 组织维护

**保护 AI 编程助手执行动作的安全检测与响应层**

Gen Digital 维护的轻量级 Agent 安全层：拦截 shell 命令、URL 抓取、文件写入等工具调用，在执行前经过多层威胁检测——云端 URL 信誉、300+ 条 YAML 本地启发式规则、双层提示注入检测（启发式+微调 ML 模型）、npm/PyPI 供应链检查、会话启动时插件扫描，以及 Windows 的 AMSI 集成。以插件/扩展形式接入 Claude Code、Cursor、VS Code、OpenClaw、OpenCode。审计日志以 JSONL 落盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拦截 shell 命令/URL/文件写入并经多层威胁检测
- 双层提示注入检测（启发式+微调 ML 模型）
- npm/PyPI 包供应链检查（注册表存在性、文件信誉、包龄分析）
- 支持 Claude Code/Cursor/VS Code/OpenClaw/OpenCode 五种宿主

## 适用场景

- 在 Claude Code 等 AI 编程助手中拦截危险命令与恶意 URL
- 防范网页内容中的提示注入指令
- 安装 npm/PyPI 包前做供应链风险检查

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L9: Sage is a lightweight security layer that protects AI agents from executing dangerous actions. It intercepts tool ca
> L17: - **Prompt injection detection** — two-tier defense (heuristics + fine-tuned ML model) against injected instruction

## 星数曲线

```mermaid
xychart-beta
    title "gendigitalinc/sage 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 315 --> 319
    line [316, 317, 318]
```

2026-10-18 316 → 2026-10-22 318（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `b8e4be7f6441` · [字段定义](../../DATASET.md)*
