# aramis-lab/clinica

⭐ 293 · Python · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/aramis-lab/clinica) · [官网](https://aramislab.paris.inria.fr/clinica/docs/public/latest) · 组织维护

**临床神经影像研究软件平台：BIDS 转换与处理流水线**

面向神经系统与精神疾病临床研究的命令行软件平台，Python 编写，基于 Nipype 做流水线编排，整合 ANTs、FreeSurfer、FSL、MRtrix、PETPVC、SPM 等神经影像分析软件包与 Scikit-learn 机器学习库。提供 ADNI、AIBL、HABS、NIFD、OASIS 等公开数据集到 BIDS 标准的转换工具，可处理任意 BIDS 兼容数据集的 T1 MRI、扩散 MRI 与 PET 数据，并衔接特征提取、统计、机器学习或深度学习。依赖的第三方工具需按所用流水线另行安装（Conda 环境文件可辅助）。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 公开数据集（ADNI/AIBL/HABS/NIFD/OASIS）到 BIDS 的转换工具
- 基于 Nipype 整合 ANTs/FreeSurfer/FSL/MRtrix/SPM 的处理流水线
- 支持 T1 MRI、扩散 MRI 与 PET 数据处理
- 特征提取与统计、机器学习、深度学习的集成

## 适用场景

- 把 ADNI 等公开神经影像数据集转换为 BIDS 格式
- 对临床神经影像数据执行标准化处理流水线
- 开展阿尔茨海默病等疾病的可复现机器学习分类研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L41: Clinica is a software platform for clinical research studies involving patients
> L71: It also provides integration between feature extraction and statistics, machine

## 星数曲线

```mermaid
xychart-beta
    title "aramis-lab/clinica 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 292 --> 294
    line [293, 293]
```

2026-10-18 293 → 2026-10-26 293（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `1cf071129f44` · [字段定义](../../DATASET.md)*
