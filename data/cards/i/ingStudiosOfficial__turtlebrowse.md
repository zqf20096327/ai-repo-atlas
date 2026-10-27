# ingStudiosOfficial/turtlebrowse

⭐ 27 · Java · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/ingStudiosOfficial/turtlebrowse) · [官网](https://turtlebrowse.ingstudios.dev) · 组织维护

**JVM 桌面浏览器，内置本地 agentic AI 与隐私功能**

基于 JCEF（Java Chromium Embedded Framework）、Swing 与 JavaFX 构建的 Material You 风格桌面浏览器，面向 Linux/Windows/macOS 多架构提供预构建下载。功能包括：100% 本地运行的 agentic AI（通过 ollama4j 包装 Ollama）、内置 Chrome DevTools、Rust 编写的广告拦截器（EasyList/UBlockOrigin 规则）、yt-dlp 视频下载、隔离用户配置、访客模式与集成终端。源码构建需 JDK 25、Node.js 与 Go。采用 Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- JCEF 嵌入式 Chromium 浏览器，支持 Chrome DevTools 协议
- 100% 本地 agentic AI，无数据外发
- Rust 广告拦截器，采用 EasyList/UBlockOrigin 等规则
- 内置终端、隔离用户配置与访客模式

## 适用场景

- 在日常浏览中使用本地 AI 助手而不上传数据
- 需要广告拦截与隐私隔离的多配置文件浏览
- 通过内置终端和 DevTools 进行开发调试

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: A Material You themed JVM based agentic browser made in JCEF (Java Chromium Embedded Framework), Swing, and JavaFX.
> L23: - 100% local agentic AI
> L32: - Available for Linux, Windows, and macOS on different architectures

## 星数曲线

```mermaid
xychart-beta
    title "ingStudiosOfficial/turtlebrowse 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25", "2026-10-27"]
    y-axis "stars" 23 --> 28
    line [24, 25, 27, 27]
```

2026-10-18 24 → 2026-10-27 27（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `bfb665d46a21` · [字段定义](../../DATASET.md)*
