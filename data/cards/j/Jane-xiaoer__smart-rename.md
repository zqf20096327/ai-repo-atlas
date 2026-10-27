# Jane-xiaoer/smart-rename

⭐ 39 · Shell · MIT · 推送 2026-04-26 · [GitHub](https://github.com/Jane-xiaoer/smart-rename) · 个人维护 · 中文 README

**macOS Finder 右键用 Gemini 给文件起中文名的工具**

面向 macOS 消费者的文件改名工具：在 Finder 中右键选中图片、视频、PDF、Word、Markdown 或文件夹，通过 macOS Quick Actions 调用 Google Gemini Flash（视觉+文本）分析内容，生成“内容关键词_日期”格式的中文名，弹出预览对话框确认后执行。BYOK 模式，用户自带 Gemini API key，100 张图约 1 分钟、成本约 $0.01。提供 CLI（preview/apply/undo/doctor）、Hammerspoon 可选热键与卸载脚本。限 macOS Monterey 及以上，跨平台版在 Roadmap。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Finder 右键 Quick Action 一键触发，支持图片/视频/PDF/Word/Markdown/文件夹
- BYOK：自带 Gemini API key，不打包任何 key
- 命名格式为内容关键词_日期，日期优先读 EXIF
- CLI 支持 --preview/--apply/--undo 撤销与 --doctor 健康检查

## 适用场景

- 把相机导出的 IMG_xxx 批量改成有意义的中文文件名
- 给笔记、扫描件、视频按内容重命名便于检索
- 批量整理下载文件夹里的乱命名文件

## 场景标签

 · 领域:桌面工具/文件管理

## 证据(README 行号)

> L3: > **中文**: 右键任何文件 → AI 自动给它起一个有意义的中文名
> L141: - Google Gemini Flash (vision + text)

## 星数曲线

```mermaid
xychart-beta
    title "Jane-xiaoer/smart-rename 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-27 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4efcc15ba070` · [字段定义](../../DATASET.md)*
