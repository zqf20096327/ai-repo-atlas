# tinqiao-oss/PocketClaw

⭐ 63 · Shell · NOASSERTION · 推送 2026-06-12 · [GitHub](https://github.com/tinqiao-oss/PocketClaw) · [官网](https://pocketclaw.cn) · 个人维护 · 中文 README

**装进 U 盘随身携带的便携个人 AI 助手（基于 OpenClaw）**

基于 OpenClaw 构建的便携式 U 盘部署方案：将 AI 助手的配置、数据与凭证全部存于 U 盘，插入电脑双击启动，自动安装 Docker/WSL2/Git 并构建容器。支持 12 家 AI 提供商（含免费推荐项），敏感信息以 AES-256-CBC + PBKDF2 加密存储，容器做了只读根文件系统、丢弃 capabilities 等加固；提供 Web/PWA 手机界面、10 种聊天软件频道接入、11 项自诊断检查、一键更新与备份。已知限制：docker inspect 可查看环境变量，忘记 Master Password 无法恢复。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 所有配置、数据与凭证自包含于 U 盘，ExFAT 三平台通用
- 12 家 AI 提供商可切换，推荐免费方案 iFlow 与智谱 GLM-4.7-Flash
- AES-256-CBC + PBKDF2 加密存储，明文仅在启动瞬间存在后擦除
- 支持 WebChat 与 Telegram/Discord/Slack 等 10 种聊天频道接入

## 适用场景

- 在多台电脑间随身携带同一个 AI 助手与个人数据
- 局域网内用手机/平板以 PWA 方式访问自己的 AI 助手
- 在常用聊天软件（如 Telegram）中直接与自己的助手对话

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L7: 本项目基于 OpenClaw（开源个人 AI 助手）构建便携式 U 盘部署方案，实现：
> L3: > 将 AI 助手装入 U 盘，随插随用，安全加密，跨平台便携。

## 星数曲线

```mermaid
xychart-beta
    title "tinqiao-oss/PocketClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-31 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d03436fa6dac` · [字段定义](../../DATASET.md)*
