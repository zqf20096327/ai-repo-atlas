# coolbirdzik/CB-File-Hub

⭐ 15 · Dart · 推送 2026-10-29 · [GitHub](https://github.com/coolbirdzik/CB-File-Hub) · 个人维护

**跨平台文件管理器，带 AI 助手做自然语言文件搜索**

基于 Flutter + Rust 的文件管理器，覆盖 Windows、macOS、Linux 与 Android。功能包括标签页浏览、分层标签与智能相册、媒体缩略图与播放、SMB/FTP/SFTP/WebDAV 网络访问与 SSH 终端、磁盘清理、种子库导入等。其中 AI 部分为 CB Agent：自然语言文件搜索、整理引导与清理审查。重扫描、搜索、缩略图、哈希等任务由 Rust 工作线程处理，README 给出 10 万文件扫描基准（84.9 ms，3.3×于 TreeSize Free）。Windows 经微软商店/MSI 提供，macOS 提供 DMG，Linux 需从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分层标签、规则式智能相册与即时搜索
- SMB/FTP/SFTP/WebDAV 网络访问与内置 SSH 终端
- CB Agent 提供自然语言文件搜索与整理引导
- Rust 工作线程处理扫描/搜索/缩略图/哈希等任务

## 适用场景

- 在桌面和手机上统一管理文件与媒体库
- 通过标签和自然语言搜索快速定位文件
- 访问局域网 SMB/WebDAV 等网络存储
- 扫描大文件夹并审查磁盘清理项

## 场景标签

 · 领域:桌面/移动文件管理工具

## 证据(README 行号)

> L5: Files, media, network access, torrents, backups, storage cleanup, and AI assistance — together in one app across des
> L37: - **CB Agent:** natural-language file search, guided organization, and cleanup review.

## 星数曲线

```mermaid
xychart-beta
    title "coolbirdzik/CB-File-Hub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e29cdfe2647b` · [字段定义](../../DATASET.md)*
