# 86maid/ddddocr

⭐ 351 · Rust · 推送 2026-04-30 · [GitHub](https://github.com/86maid/ddddocr) · 个人维护 · 中文 README

**Rust 版通用验证码 OCR 库与 API 服务，含滑块匹配**

将 Python 库 ddddocr 移植为 Rust 实现（lib.rs 为库，main.rs 为 ocr_api_server），提供单行文字 OCR、目标检测、两种滑块匹配算法与 OCR 概率输出，支持导入 dddd_trainer 训练的自定义模型，不依赖 opencv，跨平台（Windows/Linux ARM64/musl/macOS）运行。可选 cuda 特性做 GPU 推理，onnxruntime 链接库构建时自动下载。附带编译好的二进制，可作为 HTTP API 服务部署，并支持 MCP 协议供 AI Agent 调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单行文字 OCR、目标检测、两种滑块匹配算法
- OCR 概率输出与 set_ranges 字符范围限定
- 支持导入 dddd_trainer 训练的自定义模型
- HTTP API 服务（/ocr /det /slide-match 等）与 MCP 协议支持

## 适用场景

- 在 Rust 项目中集成验证码文字识别与点选目标检测
- 部署独立 OCR API 服务供其他系统调用
- 通过 MCP 让 AI Agent 调用 OCR 能力
- 做滑块验证码的缺口位置匹配

## 场景标签

`OCR` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L4: ddddocr rust 版本。
> L21:  一个容易使用的通用验证码识别 rust 库
> L65: ### 内容识别
> L116: ## 目标检测

## 星数曲线

```mermaid
xychart-beta
    title "86maid/ddddocr 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 349 --> 352
    line [350, 351, 351]
```

2026-10-18 350 → 2026-10-29 351（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1df3856cd7b0` · [字段定义](../../DATASET.md)*
