# chrisryugj/kordoc

⭐ 3,132 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/chrisryugj/kordoc) · [官网](https://pubax.org/kordoc/) · 个人维护

**让 AI 读写韩国公务文档的解析/生成库与 MCP 服务器**

将 HWP 3.x/5.x、HWPX、HWPML、PDF、Office 文档及扫描图像转为 Markdown、结构化 IR 与 RAG 分块，并支持从 Markdown 生成 HWPX/HWP 文档；附带表格比较、格式保留补丁、模板填充、新旧对照、公文预览与隐私遮罩等功能。提供 npm 库、CLI（npx 直接运行）与含 22 个工具的 MCP 服务器，可通过 setup 命令注册到 Claude Desktop、Cursor 等 MCP 客户端。支持 KORDOC_OFFLINE=1 离线模式，OCR 在本地 CPU 运行且无需 API key。需 Node.js 20+，MIT 许可。

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

- HWP·HWPX·PDF·Office·扫描图像 → Markdown/RAG 分块，Markdown → HWPX/HWP 公文
- 本地 OCR（含手写识别、逐字置信度），离线模式无需外部通信
- MCP 服务器提供 22 个工具，可注册到 Claude Desktop/Code、Cursor 等客户端
- 表格结构保留、格式保留补丁、模板填充与新旧对照功能

## 适用场景

- 把政府机关的 HWP/HWPX 公文批量转成 Markdown 供 AI 读取
- 为 RAG 索引生成带标题路径的文档分块
- 通过 MCP 让 Claude/Cursor 直接解析本地韩文公务文档
- 按机构模板批量填充公文并保留原格式

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L13: 한국 공문서를 AI가 읽고 쓸 수 있게 합니다. HWP 3.x·5.x, HWPX, HWPML, PDF, XLS·XLSX, DOCX, PPTX, 이미지(PNG·JPG·WebP·TIFF·GIF·BMP·AVIF·
> L45: |Claude Desktop·Claude Code·Cursor·Codex 등|`npx -y kordoc setup`: 설치된 클라이언트를 찾아 MCP를 등록합니다|
> L81: - **읽기**: 문서 → Markdown·IR·쪽별 본문·RAG 청크, 로컬 OCR(손글씨 인식 포함), 그림 속 QR 값(`--qr-codes`), 그림 형식 통일(`--image-format png|w

## 星数曲线

```mermaid
xychart-beta
    title "chrisryugj/kordoc 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 2675 --> 3173
    line [2716, 2726, 2751, 2786, 2808, 2826, 2832, 2851, 2873, 2882, 2726, 2939, 2958, 2966, 2975, 2991, 2994, 2995, 3013, 3022, 3038, 3051, 3066, 3084, 3106, 3115, 3132]
```

2026-10-24 2,716 → 2026-11-26 3,132（+416）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `d131ac8e3967` · [字段定义](../../DATASET.md)*
