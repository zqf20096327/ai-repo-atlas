# lobehub/lobe-assets

⭐ 27 · CSS · MIT · 推送 2026-10-28 · [GitHub](https://github.com/lobehub/lobe-assets) · 组织维护 · 中文 README

**LobeHub 的 Logo、favicon、emoji 与 Web 字体资源库**

LobeHub 维护的前端静态资源 monorepo，包含 10 个 npm 包：AI 模型品牌 Logo、favicons、静态与动画 emoji、以及 Hack Nerd Font Mono、HarmonyOS Sans（含简体中文子集包）、Geist 等 Web 字体。资源通过 npm 与 CDN 链接（npmmirror/ALIYUN-UNPKG/raw.githubusercontent）引用，HarmonyOS Sans SC Mini 用 unicode-range 拆分为基础子集与 10 个 CJK 子集。本地开发用 bun，支持 GitHub Codespaces。面向使用 LobeHub 组件（如 lobe-ui）的开发者。

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

- 10 个 npm 包覆盖 Logo/favicons/emoji/动画 emoji/Web 字体
- HarmonyOS Sans SC Mini 按 unicode-range 拆分为基础 + 10 个 CJK 子集
- favicons 提供 head 标签插入代码与 raw.githubusercontent 直链
- emoji 与字体可通过 registry.npmmirror.com CDN 直接引用

## 适用场景

- 在 LobeHub 生态项目中引用 AI 模型品牌 Logo 图标
- 网站接入 favicons 并引入 HarmonyOS Sans / Geist 等中英文字体
- 聊天界面使用静态或动画 emoji 资源

## 场景标签

 · 领域:前端设计资源

## 证据(README 行号)

> L3: Logo assets, favicons, webfonts for LobeHub
> L26: |NAME|NPM|UNPKG|
> L28: |@lobehub/assets-logo|[![][assets-logo-release]][assets-logo-release-url]|[ALIYUN-UNPKG][assets-logo-unpkg]|

## 星数曲线

```mermaid
xychart-beta
    title "lobehub/lobe-assets 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `ea60c78f4fee` · [字段定义](../../DATASET.md)*
