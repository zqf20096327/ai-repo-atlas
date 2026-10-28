# togatoga/pedaru

⭐ 113 · TypeScript · Apache-2.0 · 推送 2026-07-13 · [GitHub](https://github.com/togatoga/pedaru) · 个人维护

**带 Gemini 翻译功能的跨平台桌面 PDF 阅读器**

基于 Tauri 2.x（Rust）与 Next.js/React 构建的跨平台桌面 PDF 阅读器，提供单页/双栏视图、多标签、独立窗口、目录导航、全文搜索、书签、导航历史与会话持久化（SQLite 本地存储）等阅读功能；其中 AI 部分：选中文本后调用 Gemini 进行翻译，并可附带语法解释，翻译结果以可拖动弹窗展示。另支持连接 Google Drive 文件夹浏览和下载 PDF 书库。通过 Releases 页提供 macOS/Linux/Windows 预构建安装包，也可从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 选中文本经 Gemini 翻译，Cmd+E 附带语法解释
- 多标签、独立窗口、双栏视图与目录导航等阅读功能
- SQLite 本地存储实现会话持久化与跨会话恢复
- Google Drive 书库连接与后台下载

## 适用场景

- 阅读外文 PDF 时划词翻译并查看语法解释
- 多标签与多窗口对照阅读长文档
- 通过 Google Drive 云端同步访问 PDF 书库

## 场景标签

 · 领域:桌面工具/文档阅读

## 证据(README 行号)

> L3: A cross-platform desktop PDF reader with Gemini translation
> L110: ### 🌐 Gemini Translation

## 星数曲线

```mermaid
xychart-beta
    title "togatoga/pedaru 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-28 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `f89ea8355f45` · [字段定义](../../DATASET.md)*
