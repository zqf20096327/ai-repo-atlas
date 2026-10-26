# copybrainapp/copybrainapp

⭐ 40 · TypeScript · MIT · 推送 2026-08-27 · [GitHub](https://github.com/copybrainapp/copybrainapp) · [官网](https://www.copybrainapp.xyz/) · 个人维护

**跨平台桌面剪贴板历史归档工具，本地时间线可搜索**

基于 Tauri v2（Rust 后端 + React 前端）的剪贴板时间线应用，运行于 Windows/macOS/Linux。它将全部剪贴板历史归档到本地 SQLite 数据库，提供按日分组的时间线、FTS5 全文搜索、收藏与集合、内容类型自动检测（文本/URL/邮箱/密码掩码/代码等）及来源应用跟踪。数据完全本地存储，无网络请求。Releases 提供 dmg/msi/exe/deb/rpm/AppImage 安装包，也可从源码构建（需 Node.js 18+、pnpm 9+、Rust 及各平台编译依赖）。AI 语义搜索与 OCR 在 Roadmap 中，尚未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无限剪贴板历史本地存储于 SQLite
- FTS5 全文搜索与按日分组的时间线视图
- 内容类型自动检测，密码类默认掩码
- 100% 本地运行，无网络请求

## 适用场景

- 找回昨天、上周甚至更早复制过的内容
- 通过全文搜索快速定位历史剪贴板条目
- 关注隐私、要求剪贴板数据不出本机的用户

## 场景标签

 · 领域:桌面效率工具

## 证据(README 行号)

> L8: CopyBrain is a modern clipboard timeline application for Windows, macOS, and Linux. Unlike typical clipboard manager
> L208: - AI semantic search

## 星数曲线

```mermaid
xychart-beta
    title "copybrainapp/copybrainapp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-26 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `122eb71eaaa6` · [字段定义](../../DATASET.md)*
