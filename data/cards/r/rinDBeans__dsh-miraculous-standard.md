# rinDBeans/dsh-miraculous-standard

⭐ 12 · JavaScript · MIT · 推送 2026-08-17 · [GitHub](https://github.com/rinDBeans/dsh-miraculous-standard) · 个人维护 · 中文 README

**DeepSeek V4 Pro/Flash 的 dsh agent 锚定预设，稳定启动轨迹**

面向 DeepSeek Harness（dsh）的 agent-plane 预设插件，统一适配 DeepSeek V4 Pro/Flash × 官方 API / opencode-go 四种组合。机制：首请求仅暴露 bash+str_replace_editor 的 Minimal 锚定，晋升后按模型开放工具目录；Pro 保持最小常驻集、Flash 默认全目录；epoch 感知管理长会话，compaction 后回退受控阶段。零依赖、插件不发网络请求。自声明为社区实验项目，能力增益在独立复现中属未决。需 dsh rc.5-rc.7，Windows 需 Git for Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 双模型×双渠道统一，路径路由只看模型 id 不看 provider
- 首请求字节级 Minimal 锚定（bash + str_replace_editor，剥离自动注入）
- epoch 感知长会话管理：compaction 回退、解锁集重置、resume 去重
- 零依赖、零额外调用、零合成消息，插件均为 Node.js ESM

## 适用场景

- dsh 用户使用 DeepSeek V4 Pro/Flash 时稳定启动与长会话轨迹
- Windows 环境下解决 Git Bash 路径归一化与 PTY 缺失问题
- 通过配置键自定义晋升目录、Flash persona 与纪律提示

## 场景标签

 · 领域:LLM agent 配置/提示工程

## 证据(README 行号)

> L5: `Miraculous Standard` 是面向 DeepSeek Harness（dsh）的 agent-plane 预设。它把“首请求精确锚定”与“完整 Standard 工具能力”分离：先让 V4 Pro 稳定进入训练对齐（
> L46: 一句话：**在不放弃 Standard 完整工具面的前提下，把 DeepSeek V4 Pro / Flash 的“启动环境”稳定到 RL 对齐状态，并用 epoch 管理防止长会话轨迹漂移。**

## 星数曲线

```mermaid
xychart-beta
    title "rinDBeans/dsh-miraculous-standard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-01"]
    y-axis "stars" 11 --> 13
    line [12, 12]
```

2026-10-18 12 → 2026-11-01 12（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-01 · 置信度 high · 依据 README sha `b38e5e6e791a` · [字段定义](../../DATASET.md)*
