# tunabirgun/arf

⭐ 25 · Svelte · MIT · 推送 2026-07-15 · [GitHub](https://github.com/tunabirgun/arf) · [官网](https://tunabirgun.github.io/arf/) · 个人维护

**本地优先的笔记/第二大脑应用，设备端模型提示笔记间联系**

基于 Tauri 2 的桌面笔记应用（Windows/macOS/Linux），笔记为用户自有的纯 Markdown 文件，支持 wikilinks、双向链接、知识图谱、LaTeX 数学与代码。AI 部分：设备端 MiniLM 嵌入提供 Resonance 相似笔记推荐与每周 Synthesis 摘要，提示未链接但相关的笔记，模型可关闭。另含文献管理（Crossref/DOI/arXiv 检索、BibTeX 导出）、PDF/EPUB 侧栏阅读、云同步冲突处理与 .arf 备份。数据不出设备，无账号无服务器。

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

- 设备端 MiniLM 嵌入（约 23MB，多语版约 120MB）提供相似笔记发现与 Synthesis 配对摘要
- 纯 Markdown 文件库、wikilink 知识图谱与稳定 id 链接解析
- 文献检索/引用/多格式导出（BibTeX、RIS、APA 等）与开放获取 PDF 抓取
- 文件操作安全写入与 Dropbox/iCloud/Git 等同步冲突合并

## 适用场景

- 科研人员或开发者在本地管理带引用和数学公式的笔记
- 通过设备端模型发现自己未曾链接的相关笔记
- 在侧栏阅读 PDF/EPUB 并引用摘录到笔记中

## 场景标签

`知识库管理` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L3:  A local-first second brain for scientists and coders.
> L40: - **Discover** with the on-device model. **Resonance** surfaces notes similar to the one you are reading; the weekl
> L41: - **Read your language.** The default embedding model reads English; Settings offers a multilingual model (~120 MB)

## 星数曲线

```mermaid
xychart-beta
    title "tunabirgun/arf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6e03d5d7e47f` · [字段定义](../../DATASET.md)*
