# dushaobindoudou/dsh-plugin-security

⭐ — · [GitHub]() · 个人维护

**DeepSeek Harness 插件的安全门：审计与调用时拦截**

面向 DeepSeek Harness（dsh）插件生态的安全门插件：安装或插件变更时对已装插件做静态源码筛查与 npm 依赖通告审计，按版本+内容指纹记录并标注高风险/有风险/未发现风险；模型调用高风险插件工具时经 tools/pre-execute 钩子弹出 Allow once / Allow / Disable 询问卡片。禁用、启用、卸载调用宿主插件管理器，与原生插件页状态同步；附带 agent 技能（security_scan / security_review）供用户在对话中让 agent 审查可疑插件。需 dsh 0.2.x 与 Node.js 20+，属加载后检查而非沙箱。

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

- 静态源码筛查 + npm 依赖通告审计，按版本+内容指纹记录并自动重扫
- 调用时门控：高风险插件工具调用弹出 Allow once / Allow / Disable 询问
- 与 dsh 原生插件管理器同步禁用/启用/卸载状态
- 内置 agent 审查技能，恶意裁决仅在 enforce 模式下触发自动禁用

## 适用场景

- 安装第三方 dsh 插件前筛查恶意行为与依赖漏洞
- 模型调用高风险插件工具时逐次审批或永久放行
- 让 dsh agent 按技能流程审查可疑插件并存档裁决

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L9: A security gate for DeepSeek Harness (dsh) plugins. It scans installed plugins' source and npm dependency advisories
> L25: Requires dsh `0.2.x` (host protocol `@deepseek-ai/dsh-typert-protocol >=0.1.0-rc.6 <0.3.0`) and Node.js 20+; Node.j
> L61: The gate listens on the host `tools/pre-execute` waterfall and attributes each tool call to the plugin that registe

## 星数曲线

```mermaid
xychart-beta
    title "dushaobindoudou/dsh-plugin-security 星数(近 2 点)"
    x-axis ["2026-11-20", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-20 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `92ed55ccddfa` · [字段定义](../../DATASET.md)*
