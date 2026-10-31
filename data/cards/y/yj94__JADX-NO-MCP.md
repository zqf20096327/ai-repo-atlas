# yj94/JADX-NO-MCP

⭐ 13 · Python · 推送 2026-08-29 · [GitHub](https://github.com/yj94/JADX-NO-MCP) · 个人维护 · 中文 README

**APK 逆向分析辅助工具：整合 JADX、安全扫描并产出 AI 可读报告**

面向安全研究者的桌面 GUI 与 CLI 工具，封装 JADX 反编译、可选 apktool Smali 导出、Java 方法调用图、native .so 符号与 JNI CFG 分析（经 llvm-objdump/objdump）、签名规则式加固/壳检测及安全扫描（权限、URL/IP、危险 API、硬编码密钥）。输出紧凑的时间戳目录，含 ai_context.md、file_index.md 等文件，供人工审查或发送给 AI 助手而无需导入整个反编译 APK。要求 Python 3.9+ 与 JDK 11+，自带 jadx 与 apktool。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 反编译前的加固/壳早期检测（规则改编自 ApkCheckPack）
- Java 方法索引与 caller/callee 调用图导出
- JNI 优先的 native .so 分析（ABI 去重、CFG 提取、风险导入标记）
- 生成 ai_context.md 等面向 AI 审查的紧凑报告以降低 token 用量

## 适用场景

- 对 APK 做静态逆向与安全扫描并导出结构化报告
- 将紧凑导出目录交给 AI 助手辅助代码审查
- 在反编译前识别 APK 是否加壳以决定是否继续分析

## 场景标签

`网络安全` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: JADX-NO-MCP is a desktop and CLI helper for APK reverse engineering. It wraps JADX, optional apktool output, Java ca
> L20: - AI-focused output files such as `ai_context.md`, `file_index.md`, and compact security reports

## 星数曲线

```mermaid
xychart-beta
    title "yj94/JADX-NO-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `aa8e8cc12170` · [字段定义](../../DATASET.md)*
