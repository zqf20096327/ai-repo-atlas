# Mayachitra-Inc/MaleX

⭐ 57 · HTML · GPL-3.0 · 推送 2026-02-17 · [GitHub](https://github.com/Mayachitra-Inc/MaleX) · 组织维护

**恶意软件研究的 Windows 可执行样本图像数据集（百万级）**

面向恶意软件研究者的精选数据集：收录 1,044,394 个 Windows 可执行二进制文件及对应图像表示，其中 864,669 个标注为恶意、179,725 个为良性。提供基于字节 bi-gram 频率的 256x256 稀疏图像及经离散余弦变换（DCT）去稀疏化的 bigram-dct 图像特征，配套二进制转图像的代码。获取需填写表单，仅限研究用途；当前仅提供图像与特征，二进制文件不提供下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1,044,394 个 Windows 可执行样本及图像表示，含恶意/良性标注
- bi-gram 频率 256x256 图像 + DCT 变换的 bigram-dct 特征表示
- 提供二进制转图像的转换代码
- 数据集以 GPL-3.0 许可发布，仅限研究用途

## 适用场景

- 训练和评测基于图像的恶意软件分类模型
- 测试数据驱动机器学习方法的可扩展性与适应性
- 比较字节图像与频域图像两种恶意软件可视化方法

## 场景标签

 · 领域:网络安全/恶意软件研究

## 证据(README 行号)

> L5: _MaleX_ is a curated dataset of malware and benign Windows executable samples for malware researchers. The dataset c
> L9: The motivation to visualize malware in the frequency domain is because of the "sparse" feature representations of ma

## 星数曲线

```mermaid
xychart-beta
    title "Mayachitra-Inc/MaleX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-25 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cdffca168d10` · [字段定义](../../DATASET.md)*
