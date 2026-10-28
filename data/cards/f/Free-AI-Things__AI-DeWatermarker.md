# Free-AI-Things/AI-DeWatermarker

⭐ 21 · TypeScript · GPL-3.0 · 推送 2025-11-10 · [GitHub](https://github.com/Free-AI-Things/AI-DeWatermarker) · [官网](https://ai-de-watermarker.vercel.app) · 个人维护

**浏览器本地检测并清除 AI 水印与 Unicode 文本混淆的工具**

React + TypeScript + Vite 构建的网页工具：检测文本中的零宽字符、不可见 Unicode、同形异义字（西里尔/希腊/拉丁混用）、双向控制符、异常标点与空格等 14+ 类混淆模式，计算噪声分数并实时高亮标注，随后通过 NFC 规范化、同形字替换、控制符移除等步骤输出清洗后的文本。全部处理在浏览器本地完成，无需服务器，数据不出设备。提供在线站点使用，也可 git clone 源码后以 Node.js 18+ 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检测零宽字符、同形字、双向控制符等 14+ 类混淆模式
- 噪声分数计算与实时高亮标注、分行密度分析
- NFC 规范化与同形字替换等清洗输出
- 100% 客户端处理，无服务器调用与数据收集

## 适用场景

- 检查 AI 生成文本中隐藏的水印或追踪字符
- 清洗含不可见 Unicode 或同形字混淆的文本
- 学习 Unicode 文本混淆与检测技术

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L14: AI DeWatermarker is a free, open-source tool that detects and removes hidden AI watermarks and text obfuscation fro
> L155: - **Practical**: Clean text from AI-generated content

## 星数曲线

```mermaid
xychart-beta
    title "Free-AI-Things/AI-DeWatermarker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `bdc1594b9b19` · [字段定义](../../DATASET.md)*
