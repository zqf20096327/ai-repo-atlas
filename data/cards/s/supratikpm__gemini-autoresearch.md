# supratikpm/gemini-autoresearch

⭐ 46 · JavaScript · 推送 2026-03-27 · [GitHub](https://github.com/supratikpm/gemini-autoresearch) · 个人维护 · 中文 README

**Gemini CLI 自主迭代改进技能：设定目标后整夜自动实验并保留增益**

面向 Gemini CLI 与 Antigravity IDE 的 autoresearch 技能（skill）。用户设定目标、修改范围、度量指标与验证命令后，AI 在循环中执行“修改→验证→保留/回退”，持续迭代直到达成目标或被中断。设 Verify（进度判定）与 Guard（回归防护）双门槛，失败即回退；每 5 次成功迭代写入结构化经验（lessons），下次运行前读取以累积改进。附 plan/ship/debug/security 四个子命令与 headless 过夜模式；兼容 Claude Code、Cursor 的安装路径，Google Search grounding 仅在 Gemini 系环境生效。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 修改→验证→保留/回退的自主迭代循环，支持 headless 过夜运行
- Verify + Guard 双门槛，Guard 失败重试至多 2 次后回退
- 每 5 次成功迭代写入结构化 lessons，跨运行累积经验
- 提供 plan/ship/debug/security 子命令（STRIDE/OWASP 审计等）

## 适用场景

- 过夜自动提升测试覆盖率、压缩打包体积或消除 TypeScript 错误
- 发布前自动跑测试/类型/lint/安全检查并自动修复失败项
- 非开发者在 Antigravity IDE 中迭代改进 SEO、文案与 SOP 等可度量目标

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L26: **gemini-autoresearch** turns Gemini CLI and Antigravity IDE into an autonomous improvement engine — for anything w
> L353: ## Cross-agent compatibility

## 星数曲线

```mermaid
xychart-beta
    title "supratikpm/gemini-autoresearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `3a2c1eeb5d39` · [字段定义](../../DATASET.md)*
