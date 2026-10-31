# huangguang1999/paseo-skins

⭐ 13 · JavaScript · MIT · 推送 2026-09-21 · [GitHub](https://github.com/huangguang1999/paseo-skins) · [官网](https://huangguang1999.github.io/paseo-skins/) · 个人维护 · 中文 README

**面向 macOS Paseo 的主题皮肤画廊、构建器与 CDP 加载器**

为 macOS 上的 Paseo 应用提供换肤能力：静态网页画廊收录 259 套 DreamSkin 热门主题的适配版本（保留原作者、许可证与哈希，浏览器本地生成校验 ZIP），浏览器端 Theme Studio 可从一张本地图片自动取色生成 Theme v2 主题。CLI 通过绑定 127.0.0.1 的 Chrome DevTools Protocol 向 paseo://app/ 渲染窗口注入样式，不 patch 官方文件，支持持久模式与开机自启（launchd LaunchAgents），可随时 pause/reset 恢复原生 UI。另提供标准 Agent Skill，可被 Codex、Claude Code、Cursor 等支持 Skill 的工具调用。要求 macOS、/Applications/Paseo.app 与 Node.js 22+，Node 原生实现无运行时第三方依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CDP 仅绑定 127.0.0.1 注入样式，不 patch Paseo、不覆盖官方文件
- 浏览器本地从 PNG/JPEG/WebP 取色生成 Theme v2 主题，图片不上传
- 主题加载前校验图片类型、SHA-256、字节数与尺寸，公开 JSON Schema
- 提供 Agent Skill（npx skills add），可被 Codex/Claude Code/Cursor 调用
- 持久模式安装 launchd 登录代理，重启后自动恢复主题，可随时卸载

## 适用场景

- 给 macOS 上的 Paseo 应用更换背景主题并随时恢复原生界面
- 在浏览器里用一张图片自动生成可校验的自定义主题
- 让 AI agent 通过 Skill 接管主题选择与验收流程
- 浏览和下载带来源与许可证记录的主题画廊

## 场景标签

 · 领域:桌面定制/开发工具

## 证据(README 行号)

> L9: **Open-source Paseo themes and skins, a browser-based theme builder Studio, a live simulator, a standard Agent Skill
> L69: 安装后可直接对支持 Agent Skills 的 Codex、Claude Code、Cursor 等工具说“使用 `$paseo-skins` 换成晨雾山水”。Skill 源码位于 `skills/paseo-skins/`，网
> L61: ## Agent Skill 接入

## 星数曲线

```mermaid
xychart-beta
    title "huangguang1999/paseo-skins 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6e3810561076` · [字段定义](../../DATASET.md)*
