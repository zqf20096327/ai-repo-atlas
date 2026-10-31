# mytechnotalent/pixelproof

⭐ 17 · Python · MIT · 推送 2026-03-04 · [GitHub](https://github.com/mytechnotalent/pixelproof) · 个人维护

**检测伪造、AI 生成与修图图片的取证工具**

Python 编写的图像取证分析工具包，通过 EXIF 元数据检查、误差级别分析（ELA）、噪声一致性、颜色通道相关性、边缘密度、JPEG 量化表分析和隐写术检测（Chi-square/SPA/RS/JSteg/F5）等 10 余项检查判断图片是否被篡改或 AI 生成，输出篡改概率、置信度与融合判定，可生成 Markdown/PDF 报告与产物哈希清单。附带 stego.py 可在图片中隐藏与提取秘密消息。以命令行方式运行，供记者、法务/保险、社交媒体用户核验图片真伪。

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

- 10+ 项取证检查：EXIF、8BIM Photoshop 痕迹、ELA、噪声、颜色通道相关性、量化表
- 隐写检测含 Chi-square/SPA/RS/JSteg/F5 并带误报抑制
- 输出篡改概率、置信度、融合判定与 Markdown/PDF 报告
- stego.py 支持图片内消息隐藏与提取

## 适用场景

- 核验收到的照片是真实拍摄还是伪造
- 法律/保险场景留存图片篡改取证证据
- 发布前核验新闻来源图片
- 检查病毒式传播照片是否为 AI 生成或修图

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: **Detect fake, AI-generated, and Photoshopped images in seconds.**
> L9: PixelProof is a forensic-grade image analysis toolkit that exposes manipulation through metadata inspection, Error L
> L31: |**Steganography Detection**|Chi-square, SPA, RS, bit-plane entropy, and JPEG DCT-level (JSteg/F5) analysis with fa

## 星数曲线

```mermaid
xychart-beta
    title "mytechnotalent/pixelproof 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `2209453dc0a1` · [字段定义](../../DATASET.md)*
