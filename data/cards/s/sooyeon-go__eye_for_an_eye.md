# sooyeon-go/eye_for_an_eye

⭐ 35 · Jupyter Notebook · 推送 2026-03-09 · [GitHub](https://github.com/sooyeon-go/eye_for_an_eye) · 个人维护

**论文官方实现：扩散模型中按语义对应做外观迁移**

WACV 2026 论文 Eye-for-an-eye 的官方代码实现：在文本到图像扩散模型中，生成保持目标图像结构、但按语义对应关系从参考图取色的结果（如结果翅膀取参考图翅膀的颜色）。方法通过寻找语义对应并显式重排特征实现，基于 diffusers 库构建，使用 DIFT 的对应匹配方法。提供 conda 环境配置、边界框生成 notebook 与单对象版本运行脚本；多对象版本与 Demo 标注为 coming soon。可选安装 SAM-HQ 用于提取实例掩码，不用掩码时无法保留目标图背景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按语义对应从参考图向结果迁移颜色，保持目标图结构
- 基于 diffusers 库，采用 DIFT 对应匹配方法
- 可选接入 SAM-HQ 提取实例掩码以保留背景
- 提供 guidance scale、feat_range、adain_range 等参数调节

## 适用场景

- 将参考图像的外观按语义对应迁移到目标图像结构上
- 复现或研究扩散模型中的外观/风格迁移方法
- 对比 V 注入与特征注入两种机制的差异

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L14: Official implementation of our Eye-for-an-eye: Appearance Transfer with Semantic Correspondence in Diffusion Models
> L9: As pretrained text-to-image diffusion models have become a useful tool for image synthesis, people want to specify t

## 星数曲线

```mermaid
xychart-beta
    title "sooyeon-go/eye_for_an_eye 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `526fe2572090` · [字段定义](../../DATASET.md)*
