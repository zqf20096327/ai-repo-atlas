# tcsenpai/qrare

⭐ 38 · Python · 推送 2026-09-08 · [GitHub](https://github.com/tcsenpai/qrare) · 个人维护

**把二进制文件转成 QR 码图片并可还原的 Python CLI 工具**

用于在任意二进制文件与 QR 码图片之间双向转换的 Python 命令行工具：编码时读取文件、zlib 压缩、按可配置大小分块，每块附带索引/总数/文件名/哈希元数据生成 QR 码 PNG；解码时扫描校验、按序重组、解压并用 SHA-256 验证完整性。提供 fast/compact/robust 预设、analyze 与估算命令，也支持以 Python 库形式调用。README 未出现 AI/LLM 相关功能，主题标签中的 ai/llm 在正文无对应内容。运行需安装 ZBar 系统库用于 QR 读取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文件↔QR 码双向转换，含 zlib 压缩与 SHA-256 完整性校验
- 可配置分块大小、QR 版本(1-40)、压缩级别与纠错级别
- fast/compact/robust 三种预设及 analyze 分析/估算命令
- 提供 CLI 与程序化 API（BinaryQRConverter 等模块化类）

## 适用场景

- 把文件以 QR 码图片形式离线传递或归档
- 扫描后无损还原原始二进制文件并校验完整性
- 批量处理多个文件的编码转换

## 场景标签

 · 领域:文件转换/命令行工具

## 证据(README 行号)

> L3: A powerful and modular Python CLI tool for converting binary files to QR codes and reconstructing them back to the o
> L211: 1. **📁 File Reading**: Binary file is read into memory
> L223: 5. **🔒 Verification**: SHA-256 hash confirms file integrity

## 星数曲线

```mermaid
xychart-beta
    title "tcsenpai/qrare 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6b50d33ec845` · [字段定义](../../DATASET.md)*
