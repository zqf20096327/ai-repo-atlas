# jammaru/sakutto

⭐ 307 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/jammaru/sakutto) · [官网](https://chrome.google.com/webstore/detail/mhlbjjijfkoghmcjndgdimhdlfkhadfl) · 个人维护

**浏览器本地翻译扩展：用 PLaMo 在设备上翻译网页/PDF/视频/输入**

非官方 Chrome/Firefox 扩展，默认引擎为 PLaMo 3 Translate，通过固定版本的 wllama 构建在 WebGPU 或 CPU 上运行，翻译过程在用户设备本地完成、可离线使用。支持整页替换或双语视图、选中文本、输入框文字（Alt+T）、Gmail/Outlook 邮件横幅、保留版式的 PDF 翻译（无文本层的扫描页用 PP-OCRv6 本地 OCR）、YouTube/X 视频字幕覆盖翻译、全局与按站点术语表（CSV 导入导出）以及「易日语」目标。模型权重从 Hugging Face 下载（默认 0.8B 约 546 MB），无账号、无遥测。Chrome 上另有 11 个目标语言由 Chrome 内置翻译器处理；Firefox 仅用 PLaMo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认 PLaMo 引擎本地运行，53 种语言双向翻译，可离线
- 保留版式的 PDF 翻译，扫描页用本地 PP-OCRv6 识别
- 视频字幕（YouTube 含直播、X）播放时覆盖翻译
- 全局/站点术语表与易日语目标，实验性本地 OpenAI 兼容服务器后端

## 适用场景

- 在浏览外文网页和论文 PDF 时整页翻译且文本不出设备
- 看 YouTube/X 视频时实时翻译字幕
- 写邮件或消息前把草稿翻成目标语言再替换
- 用术语表固定产品名和术语的译法

## 场景标签

 · 领域:浏览器工具/翻译

## 证据(README 行号)

> L16: Sakutto is an unofficial Chrome and Firefox extension that translates web pages, PDFs (including scans), images, vi
> L18: For PLaMo's 53 languages, every translated line comes from PLaMo. On Chrome, Chrome's built-in translator is used o
> L90: 3. Accept the PLaMo licence and let the one-time model download finish. After that, translation runs on your device

## 星数曲线

```mermaid
xychart-beta
    title "jammaru/sakutto 星数(近 17 点)"
    x-axis ["2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 180 --> 318
    line [191, 218, 234, 238, 240, 252, 258, 264, 272, 275, 274, 279, 282, 284, 304, 307, 307]
```

2026-11-10 191 → 2026-11-28 307（+116）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `b2f278752860` · [字段定义](../../DATASET.md)*
