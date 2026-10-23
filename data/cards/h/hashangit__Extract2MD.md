# hashangit/Extract2MD

⭐ 108 · JavaScript · MIT · 推送 2026-04-07 · [GitHub](https://github.com/hashangit/Extract2MD) · [官网](https://www.inferencequotient.com) · 个人维护

**浏览器端 PDF 转 Markdown 的 JS 库，含可选 LLM 增强**

客户端 JavaScript/TypeScript 库，提供 5 种转换场景：PDF.js 文本提取、Tesseract.js OCR、以及两者与 WebLLM（浏览器内 LLM，Qwen 模型）组合的 AI 增强转换。输出 Markdown，支持自定义系统提示词、JSON 配置与校验、进度回调、旧版 API 兼容。通过 npm 或 CDN 安装，需部署 PDF.js 与 Tesseract.js worker 文件，完整包约 11 MB。

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

- 5 种场景化转换方法（纯提取/OCR/+LLM 组合）
- WebLLM 浏览器内 AI 增强，默认 Qwen 模型，支持自定义模型
- 完整 TypeScript 类型定义与进度跟踪回调
- 提供 npm 与 CDN 两种安装方式

## 适用场景

- 在网页应用中将用户上传的 PDF 转为 Markdown
- 处理扫描件或含图片 PDF 的 OCR 转换
- 在浏览器端不依赖服务器完成 LLM 增强的格式化转换

## 场景标签

`文档解析` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L41: - **Tech**: PDF.js + WebLLM
> L121: - **WebLLM Integration**: Client-side AI enhancement with Qwen models

## 星数曲线

```mermaid
xychart-beta
    title "hashangit/Extract2MD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-23 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1fb15e671c69` · [字段定义](../../DATASET.md)*
